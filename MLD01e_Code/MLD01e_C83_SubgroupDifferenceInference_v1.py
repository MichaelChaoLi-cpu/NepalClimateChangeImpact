"""Minimal inference for the subgroup contrasts displayed in Figures 4–7.

The analysis supplements the existing graphical evidence for Reviewer 2
Comment 13 without introducing a separate outcome model:

* six total-effect outcomes already displayed in each subgroup figure;
* four figure-defined subgroup contrasts, giving 24 panel-level comparisons;
* one cluster-robust difference-in-means model per figure panel;
* standard errors clustered by survey-year PSU;
* Holm adjustment across the 24 displayed comparisons.

The dependent variable is each observation's counterfactual minus factual
probability, using the mean of the ten repeated out-of-fold predictions. The
resulting inference is conditional on the fitted prediction models and does
not propagate their full estimation uncertainty.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
from openpyxl.styles import Alignment, Border, Font, Side
from openpyxl.utils import get_column_letter
from statsmodels.stats.multitest import multipletests

import LoadDataFromDisk


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_ROOT / "MLD01e_Results" / "MLD01e1_Results"
CSV_OUTPUT = RESULTS_DIR / "Table_SubgroupDifferenceInference.csv"
XLSX_OUTPUT = RESULTS_DIR / "Table_SubgroupDifferenceInference.xlsx"

TABLE_TITLE = (
    "Cluster-robust comparisons of subgroup differences in model-estimated total effects"
)
TABLE_NOTE = (
    "Notes: Total effects are individual differences between counterfactual and factual "
    "predicted probabilities averaged across 10 repeated out-of-fold predictions. Each "
    "subgroup difference equals the focal-group mean minus the reference-group mean and "
    "is tested using a separate OLS with a subgroup indicator. Standard errors are "
    "clustered at the survey-year–PSU level, and the Holm procedure adjusts p-values "
    "across the 24 comparisons. Focal/reference groups are Female/Male for Gender, "
    "Age >65/Age 45–65 for Age, Low income/High income for Income, and Rural/Urban for "
    "Location. Inference is conditional on the fitted prediction models."
)

EXPECTED_N = 11_568
INCOME_THRESHOLD = 170_000.0

OUTCOMES = {
    "Climate knowledge": (
        "factual_knowledge_probs.parquet",
        "counterfactual_knowledge_probs.parquet",
    ),
    "Climate awareness": (
        "factual_awareness_probs.parquet",
        "counterfactual_awareness_probs.parquet",
    ),
    "Soil and water conservation": (
        "factual_action_probs_soilandwater.parquet",
        "counterfactual_action_probs_soilandwater.parquet",
    ),
    "Risk reduction": (
        "factual_action_probs_riskreduction.parquet",
        "counterfactual_action_probs_riskreduction.parquet",
    ),
    "Road improvement": (
        "factual_action_probs_roadimprovement.parquet",
        "counterfactual_action_probs_roadimprovement.parquet",
    ),
    "Community participation": (
        "factual_action_probs_communityparticipation.parquet",
        "counterfactual_action_probs_communityparticipation.parquet",
    ),
}

CONTRASTS = {
    "female": ("Female", "Male", 4),
    "older_than_65": ("Age >65", "Age 45–65", 5),
    "low_income": ("Low income (≤170,000)", "High income (>170,000)", 6),
    "rural": ("Rural", "Urban", 7),
}

PANEL_LETTERS = dict(zip(OUTCOMES, "abcdef", strict=True))
GROUP_DIMENSIONS = {
    4: "Gender",
    5: "Age",
    6: "Income",
    7: "Location",
}


def _read_probability(path: Path) -> pd.DataFrame:
    frame = pd.read_parquet(path)
    expected_columns = [str(i) for i in range(10)] + ["mean"]
    if list(frame.columns) != expected_columns:
        raise ValueError(f"Unexpected probability columns in {path}: {list(frame.columns)}")
    if len(frame) != EXPECTED_N:
        raise ValueError(f"Unexpected row count in {path}: {len(frame)}")
    repeated_mean = frame[[str(i) for i in range(10)]].mean(axis=1)
    if not np.allclose(frame["mean"], repeated_mean, rtol=0.0, atol=1e-12):
        raise ValueError(f"The mean column does not equal the ten repeated predictions in {path}")
    return frame


def _load_analysis_data() -> tuple[pd.DataFrame, dict[str, pd.Series]]:
    data = LoadDataFromDisk.load_data_from_disk().reset_index()
    if len(data) != EXPECTED_N:
        raise ValueError(f"Unexpected analysis-data row count: {len(data)}")

    data = data.assign(
        female=data["Respon_Female"].astype(int),
        older_than_65=(data["Respon_Age"] > 65).astype(int),
        low_income=(data["TotalIncome"] <= INCOME_THRESHOLD).astype(int),
        rural=data["Rural_Dummy"].astype(int),
        cluster_id=data["Year"].astype(str) + ":" + data["PSU"].astype(str),
    )

    effects: dict[str, pd.Series] = {}
    for outcome, (factual_name, counterfactual_name) in OUTCOMES.items():
        factual = _read_probability(RESULTS_DIR / factual_name)
        counterfactual = _read_probability(RESULTS_DIR / counterfactual_name)
        effect = counterfactual["mean"] - factual["mean"]
        if effect.isna().any() or not np.isfinite(effect).all():
            raise ValueError(f"Non-finite total effects for {outcome}")
        effects[outcome] = effect

    return data, effects


def _fit_panel_comparison(
    data: pd.DataFrame,
    effect: pd.Series,
    outcome: str,
    contrast: str,
    focal_label: str,
    reference_label: str,
    figure_number: int,
) -> dict[str, object]:
    design = sm.add_constant(data[[contrast]], has_constant="add")
    model = sm.OLS(effect.to_numpy(), design).fit(
        cov_type="cluster",
        cov_kwds={
            "groups": data["cluster_id"],
            "use_correction": True,
            "df_correction": True,
        },
        use_t=True,
    )

    group = data[contrast].astype(bool)
    focal_mean = float(effect[group].mean() * 100)
    reference_mean = float(effect[~group].mean() * 100)
    difference = focal_mean - reference_mean
    coefficient = float(model.params[contrast] * 100)
    if not np.isclose(coefficient, difference, rtol=0.0, atol=1e-12):
        raise ValueError(f"Model coefficient does not match displayed mean difference: {outcome}")
    confidence_interval = model.conf_int().loc[contrast]
    return {
        "figure_panel": f"Figure {figure_number}{PANEL_LETTERS[outcome]}",
        "outcome": outcome,
        "contrast": f"{focal_label} − {reference_label}",
        "coefficient": contrast,
        "focal_group": focal_label,
        "reference_group": reference_label,
        "focal_n": int(group.sum()),
        "reference_n": int((~group).sum()),
        "focal_mean_total_effect_pp": focal_mean,
        "reference_mean_total_effect_pp": reference_mean,
        "difference_pp": coefficient,
        "cluster_robust_se_pp": float(model.bse[contrast] * 100),
        "ci95_lower_pp": float(confidence_interval.iloc[0] * 100),
        "ci95_upper_pp": float(confidence_interval.iloc[1] * 100),
        "raw_p_value": float(model.pvalues[contrast]),
        "n_observations": int(model.nobs),
        "n_clusters": int(data["cluster_id"].nunique()),
        "inference_degrees_of_freedom": float(model.df_resid_inference),
        "model_r_squared": float(model.rsquared),
    }


def run_analysis() -> pd.DataFrame:
    data, effects = _load_analysis_data()
    rows: list[dict[str, object]] = []
    for contrast, (focal_label, reference_label, figure_number) in CONTRASTS.items():
        for outcome, effect in effects.items():
            rows.append(
                _fit_panel_comparison(
                    data,
                    effect,
                    outcome,
                    contrast,
                    focal_label,
                    reference_label,
                    figure_number,
                )
            )

    results = pd.DataFrame(rows)
    if len(results) != len(OUTCOMES) * len(CONTRASTS):
        raise ValueError(f"Expected 24 comparisons, found {len(results)}")

    reject, adjusted_p, _, _ = multipletests(
        results["raw_p_value"].to_numpy(), alpha=0.05, method="holm"
    )
    results["holm_adjusted_p_value"] = adjusted_p
    results["significant_after_holm_0_05"] = reject
    results["inference_scope"] = (
        "Conditional on averaged repeated out-of-fold predictions; "
        "does not propagate full model-fitting uncertainty"
    )
    return results


def _specification_table(data: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "item": [
                "Estimand",
                "Outcomes",
                "Contrasts",
                "Regression",
                "Cluster",
                "Multiple comparisons",
                "Age definition",
                "Income definition",
                "Uncertainty boundary",
                "Observations",
                "Clusters",
            ],
            "specification": [
                "Individual counterfactual minus factual total effect",
                "Six total-effect outcomes displayed in each of Figures 4–7",
                "Female−male; age >65−age 45–65; low−high income; rural−urban",
                "One difference-in-means OLS per figure panel: total effect ~ focal indicator",
                "Standard errors clustered by survey-year PSU with finite-sample correction",
                "Holm family-wise adjustment across all 24 displayed panel comparisons",
                "Older group is age >65; reference group is age 45–65",
                "Low income ≤170,000; high income >170,000",
                "Conditional on averaged repeated out-of-fold predictions",
                str(len(data)),
                str(data["cluster_id"].nunique()),
            ],
        }
    )


def _group_counts(data: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for contrast, (focal_label, reference_label, _) in CONTRASTS.items():
        group = data[contrast].astype(bool)
        rows.extend(
            [
                {"contrast_variable": contrast, "group": focal_label, "n": int(group.sum())},
                {
                    "contrast_variable": contrast,
                    "group": reference_label,
                    "n": int((~group).sum()),
                },
            ]
        )
    return pd.DataFrame(rows)


def _reporting_table(results: pd.DataFrame) -> pd.DataFrame:
    table = results[
        [
            "outcome",
            "figure_panel",
            "contrast",
            "focal_mean_total_effect_pp",
            "reference_mean_total_effect_pp",
            "difference_pp",
            "ci95_lower_pp",
            "ci95_upper_pp",
            "raw_p_value",
            "holm_adjusted_p_value",
            "significant_after_holm_0_05",
        ]
    ].copy()
    table["difference_with_95ci_pp"] = table.apply(
        lambda row: (
            f"{row['difference_pp']:.3f} "
            f"[{row['ci95_lower_pp']:.3f}, {row['ci95_upper_pp']:.3f}]"
        ),
        axis=1,
    )
    table["group_dimension"] = (
        table["figure_panel"].str.extract(r"Figure (\d+)", expand=False).astype(int)
        .map(GROUP_DIMENSIONS)
    )
    table["holm_p_display"] = table["holm_adjusted_p_value"].map(
        lambda value: f"{value:.3f}"
    )
    table = table[
        [
            "group_dimension",
            "outcome",
            "focal_mean_total_effect_pp",
            "reference_mean_total_effect_pp",
            "difference_with_95ci_pp",
            "holm_p_display",
        ]
    ]
    return table.rename(
        columns={
            "group_dimension": "Group",
            "outcome": "Outcome",
            "focal_mean_total_effect_pp": "Focal effect (pp)",
            "reference_mean_total_effect_pp": "Reference effect (pp)",
            "difference_with_95ci_pp": "Difference [95% CI] (pp)",
            "holm_p_display": "Holm-adjusted p",
        }
    )


def _apply_academic_table_style(writer: pd.ExcelWriter) -> None:
    workbook = writer.book
    thin_black = Side(style="thin", color="000000")
    medium_black = Side(style="medium", color="000000")
    body_font = Font(name="Times New Roman", size=10, color="000000")
    header_font = Font(name="Times New Roman", size=10, bold=True, color="000000")

    for worksheet in workbook.worksheets:
        worksheet.sheet_view.showGridLines = False
        worksheet.freeze_panes = "A2"
        worksheet.page_setup.orientation = "landscape"
        worksheet.page_setup.fitToWidth = 1
        worksheet.page_setup.fitToHeight = 0
        worksheet.sheet_properties.pageSetUpPr.fitToPage = True
        worksheet.page_margins.left = 0.25
        worksheet.page_margins.right = 0.25
        worksheet.page_margins.top = 0.5
        worksheet.page_margins.bottom = 0.5

        for row in worksheet.iter_rows():
            for cell in row:
                cell.font = body_font
                cell.alignment = Alignment(vertical="center")

        for cell in worksheet[1]:
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            cell.border = Border(top=medium_black, bottom=thin_black)

        if worksheet.max_row >= 2:
            for cell in worksheet[worksheet.max_row]:
                cell.border = Border(bottom=medium_black)

        worksheet.row_dimensions[1].height = 30
        worksheet.auto_filter.ref = worksheet.dimensions

    reporting = workbook["Reporting table"]
    reporting.freeze_panes = "A2"
    reporting.column_dimensions["A"].width = 10
    reporting.column_dimensions["B"].width = 27
    reporting.column_dimensions["C"].width = 15
    reporting.column_dimensions["D"].width = 17
    reporting.column_dimensions["E"].width = 23
    reporting.column_dimensions["F"].width = 14
    reporting.print_area = f"A1:F{reporting.max_row}"
    reporting.sheet_properties.pageSetUpPr.fitToPage = True
    reporting.page_setup.paperSize = reporting.PAPERSIZE_A4

    for row_number in range(2, reporting.max_row + 1):
        reporting.row_dimensions[row_number].height = 18
        reporting.cell(row_number, 1).alignment = Alignment(horizontal="left", vertical="center")
        reporting.cell(row_number, 2).alignment = Alignment(horizontal="left", vertical="center")
        for column_number in (3, 4, 5, 6):
            reporting.cell(row_number, column_number).alignment = Alignment(
                horizontal="center", vertical="center"
            )
        for column_number in (3, 4):
            reporting.cell(row_number, column_number).number_format = "0.000"
        reporting.cell(row_number, 6).number_format = "0.000"

        if row_number > 2 and reporting.cell(row_number, 1).value != reporting.cell(
            row_number - 1, 1
        ).value:
            for cell in reporting[row_number]:
                cell.border = Border(top=thin_black)

    notes = workbook["Table note"]
    notes.freeze_panes = None
    notes.auto_filter.ref = None
    notes.column_dimensions["A"].width = 28
    notes.column_dimensions["B"].width = 110
    notes.row_dimensions[2].height = 72
    for cell in notes[2]:
        cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

    inference = workbook["Inference"]
    for column_number in range(1, inference.max_column + 1):
        inference.column_dimensions[get_column_letter(column_number)].width = 18
    for row_number in range(2, inference.max_row + 1):
        for column_number in range(1, inference.max_column + 1):
            cell = inference.cell(row_number, column_number)
            if isinstance(cell.value, float):
                cell.number_format = "0.000"
        adjusted_p_column = next(
            cell.column for cell in inference[1] if cell.value == "holm_adjusted_p_value"
        )
        inference.cell(row_number, adjusted_p_column).number_format = "0.000"

    specification = workbook["Specification"]
    specification.column_dimensions["A"].width = 28
    specification.column_dimensions["B"].width = 105
    for row in specification.iter_rows(min_row=2):
        row[1].alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    counts = workbook["Group counts"]
    counts.column_dimensions["A"].width = 24
    counts.column_dimensions["B"].width = 25
    counts.column_dimensions["C"].width = 12
    for row_number in range(2, counts.max_row + 1):
        counts.cell(row_number, 3).number_format = "0"


def main() -> None:
    data, _ = _load_analysis_data()
    results = run_analysis()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    results.to_csv(CSV_OUTPUT, index=False)
    with pd.ExcelWriter(XLSX_OUTPUT, engine="openpyxl") as writer:
        _reporting_table(results).to_excel(writer, sheet_name="Reporting table", index=False)
        pd.DataFrame({"Table title": [TABLE_TITLE], "Table note": [TABLE_NOTE]}).to_excel(
            writer, sheet_name="Table note", index=False
        )
        results.to_excel(writer, sheet_name="Inference", index=False)
        _specification_table(data).to_excel(writer, sheet_name="Specification", index=False)
        _group_counts(data).to_excel(writer, sheet_name="Group counts", index=False)
        _apply_academic_table_style(writer)

    supported = int(results["significant_after_holm_0_05"].sum())
    print(f"Wrote {CSV_OUTPUT}")
    print(f"Wrote {XLSX_OUTPUT}")
    print(f"Holm-significant comparisons: {supported}/{len(results)}")


if __name__ == "__main__":
    main()
