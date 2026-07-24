import geopandas as gpd
import math
import matplotlib as mpl
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import numpy as np
import os, sys
import pandas as pd

from glob import glob
from matplotlib import cm

def load_spatial_data() -> gpd.GeoDataFrame:
    """
    Load and combine Nepal EcoBelt and Province spatial data.

    This function:
    1. Loads the EcoBelt shapefile (3-class version: Mountain, Hill, Terai).
    2. Loads the Province shapefile.
    3. Converts both to the same CRS (EPSG:4326, WGS84).
    4. Computes the spatial intersection between EcoBelts and Provinces.

    Returns:
        gpd.GeoDataFrame: A GeoDataFrame containing intersected polygons
                          with both EcoBelt and Province attributes.
    """
    # --- Load EcoBelt shapefile ---
    gdf_eco = gpd.read_file('PrivateData/SpatialMaps/nepal_ecobelt_data/3_class_shape/Ecobelts_3Class.shp')
    gdf_eco = gdf_eco.to_crs(epsg=4326)

    # --- Load Province shapefile ---
    gdf_nepal = gpd.read_file('PrivateData/SpatialMaps/02_PROVINCE/PROVINCE.shp')
    gdf_nepal = gdf_nepal[['geometry', 'Province']].to_crs(epsg=4326)

    # --- Intersection ---
    try:
        gdf_intersect = gpd.overlay(gdf_eco, gdf_nepal, how='intersection')
    except Exception as e:
        raise RuntimeError(f"❌ Failed to overlay EcoBelt and Province shapefiles: {e}")

    # --- Optional cleanup ---
    gdf_intersect = gdf_intersect.rename(columns={'EcoBelt': 'Eco_Belt'}) if 'EcoBelt' in gdf_intersect.columns else gdf_intersect

    print(f"✅ Loaded spatial data with {len(gdf_intersect)} intersected polygons.")
    return gdf_intersect

def build_province_diff_df(
    probs_dictionary: dict[str, pd.DataFrame],
    input_name_list: list[str],
    province_column: pd.Series,
    ecobelt_column: pd.Series
) -> pd.DataFrame:
    """
    Build a DataFrame of mean probability differences (factual - counterfactual)
    across all Province × EcoBelt combinations for each variable in input_name_list.

    Args:
        probs_dictionary (dict): Dictionary with factual and counterfactual DataFrames.
        input_name_list (list): List of input variable names (without 'counter' prefix).
        province_column (pd.Series): Province label for each observation.
        ecobelt_column (pd.Series): EcoBelt label for each observation.

    Returns:
        pd.DataFrame: A DataFrame where rows are Province–EcoBelt combinations,
                      and columns are input names.
    """
    province_list = sorted(province_column.unique())
    ecobelt_list = sorted(ecobelt_column.unique())

    # Create a combined index of Province × EcoBelt
    index_pairs = [(prov, eco) for prov in province_list for eco in ecobelt_list]

    # Prepare an empty DataFrame
    df_diff = pd.DataFrame(index=pd.MultiIndex.from_tuples(index_pairs, names=["Province", "EcoBelt"]),
                           columns=input_name_list, dtype=float)

    # Convert to arrays once for speed
    prov_arr = province_column.to_numpy()
    eco_arr = ecobelt_column.to_numpy()

    # Main computation
    for input_name in input_name_list:
        factual_df = probs_dictionary[input_name].copy()
        counterfactual_df = probs_dictionary[f'counter{input_name}'].copy()

        factual_df['Province'] = prov_arr
        factual_df['EcoBelt'] = eco_arr
        counterfactual_df['Province'] = prov_arr
        counterfactual_df['EcoBelt'] = eco_arr

        for prov, eco in index_pairs:
            mask_factual = (factual_df['Province'] == prov) & (factual_df['EcoBelt'] == eco)
            mask_counter = (counterfactual_df['Province'] == prov) & (counterfactual_df['EcoBelt'] == eco)

            if mask_factual.sum() > 0 and mask_counter.sum() > 0:
                diff = counterfactual_df.loc[mask_factual, 'mean'].mean() - factual_df.loc[mask_counter, 'mean'].mean()
            else:
                diff = float('nan')

            df_diff.loc[(prov, eco), input_name] = diff

    return df_diff


def plot_spatial_differences(map_diff_df: gpd.GeoDataFrame, save_address: str):
    """
    Plot spatial differences for each variable in the GeoDataFrame.

    Args:
        map_diff_df (gpd.GeoDataFrame): GeoDataFrame with spatial data and differences.
        save_address (str): File path to save the resulting figure.
    """
    # Define per-column vmin/vmax
    vmaxs = [0.060, 0.030, 0.020, 0.010, 0.030, 0.030]
    vmins = [0.030, 0.005, 0, 0, 0, 0]

    # Prepare subplots (2 rows × 3 columns)
    fig, axes = plt.subplots(3, 2, figsize=(18, 15))
    axes = axes.flatten()

    # Colormap
    cmap = plt.cm.RdYlBu_r
    sub_figure_code = list("abcdefghijklmnopqrstuvwxyz")

    # Plot each variable
    for idx, col in enumerate(map_diff_df.columns[:6]):
        ax = axes[idx]

        # Plot GeoDataFrame without legend
        map_diff_df.plot(
            column=col,
            cmap=cmap,
            edgecolor='black',
            linewidth=0.4,
            vmin=vmins[idx],
            vmax=vmaxs[idx],
            alpha=0.8,
            legend=False,
            ax=ax
        )

        # Create a colorbar manually with matching height
        sm = mpl.cm.ScalarMappable(
            norm=mpl.colors.Normalize(vmin=vmins[idx], vmax=vmaxs[idx]),
            cmap=cmap
        )
        sm._A = []  # required for ScalarMappable
        cbar = fig.colorbar(sm, ax=ax, fraction=0.030, pad=0.02)  # adjust height
        cbar.ax.tick_params(labelsize=8)

        # Style
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.grid(True, linestyle='-', alpha=0.4)
        ax.axis('on')
        ax.text(
            0.02, 0.95, f"({sub_figure_code[idx]})",
            transform=ax.transAxes, fontsize=18,
            fontweight='bold', va='top', color='black'
        )
    # Remove empty subplot(s)
    for ax in axes[len(map_diff_df.columns[:6]):]:
        ax.axis('off')

    plt.tight_layout()
    plt.savefig(save_address, dpi=300, bbox_inches='tight')
    plt.show()

    print(f"✅ Violin plots saved to: {save_address}")
