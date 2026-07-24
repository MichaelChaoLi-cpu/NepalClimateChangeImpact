import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedKFold
from typing import Tuple
from xgboost import XGBClassifier


def predicting_counter_and_factual_knowledge_based_xgboost(
    df_inuse: 'pd.DataFrame'
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Perform counterfactual and factual prediction of climate change knowledge using XGBoost.

    This function uses an XGBoost classifier to predict the probability of having climate change knowledge (factual)
    and the probability under a counterfactual scenario where education year is increased by 1 and literacy dummies are set to 0.
    It performs repeated stratified 10-fold cross-validation with different random seeds, using the best hyperparameters from a previous search.
    The function returns the probability matrices for both factual and counterfactual predictions, with mean probabilities across folds.

    Args:
        df_inuse (pd.DataFrame): Input DataFrame with features and the target column 'Heard about Climate Change Dummy'.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]:
            - prob_matrix: Factual prediction probabilities for each sample (mean across folds).
            - prob_matrix_tide: Counterfactual prediction probabilities for each sample (mean across folds).
    """
    # Extract target and features
    y = df_inuse['Heard about Climate Change Dummy'].astype(int)
    X = df_inuse.drop(columns=['Heard about Climate Change Dummy'])

    # Calculate class imbalance weight
    pos = y.sum()
    neg = len(y) - pos
    scale_pos_weight = (neg / pos) if pos > 0 else 1.0

    # Load best hyperparameters from previous search
    cvres = pd.read_parquet('MLD01e_Results/MLD01e_C01_KnowledgeFactorInvestigation.parquet')
    params = cvres.sort_values('rank_test_score').iloc[0,10]

    # Initialize probability matrices
    prob_matrix = pd.DataFrame(np.zeros([X.shape[0], 10]))
    prob_matrix_tide = pd.DataFrame(np.zeros([X.shape[0], 10]))

    # Repeated stratified 10-fold cross-validation
    for epoch, random_seed in enumerate(range(42, 42*11, 42)):
        cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=random_seed)
        for fold, (train_idx, test_idx) in enumerate(cv.split(X, y), 1):
            X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
            y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
            # Ensure test columns match train columns
            X_test = X_test.reindex(columns=X_train.columns, fill_value=0)
            pos = y_train.sum()
            neg = len(y_train) - pos
            scale_pos_weight = (neg / pos) if pos > 0 else 1.0
            
            # Train XGBoost classifier
            clf = XGBClassifier(objective="binary:logistic",
                                eval_metric="logloss", tree_method="hist", 
                                random_state=random_seed, 
                                scale_pos_weight=scale_pos_weight, device = 'cuda',
                                **params)
            clf.fit(X_train, y_train)
            # Factual prediction
            prob_matrix.iloc[test_idx, epoch] = clf.predict_proba(X_test)[:, 1]
            # Counterfactual: increase education year, set literacy dummies to 0
            X_tide = X_test.copy()
            X_tide['Education Year'] = X_tide['Education Year'] + 1
            X_tide['Literate Education Dummy'] = 0
            X_tide['Illiterate Dummy'] = 0
            prob_matrix_tide.iloc[test_idx, epoch] = clf.predict_proba(X_tide)[:, 1]
        print(f'epoch: {epoch}, random_seed:{random_seed}')

    # Calculate mean probability across folds
    prob_matrix['mean'] = prob_matrix.mean(axis=1)
    prob_matrix_tide['mean'] = prob_matrix_tide.mean(axis=1)

    return prob_matrix, prob_matrix_tide

def predicting_counter_and_factual_awareness_based_xgboost(
    df_inuse: 'pd.DataFrame',
    factural_knowledge_probs: 'pd.DataFrame',
    counterfactual_knowledge_probs: 'pd.DataFrame',
    direct_impact: bool = True,
    indirect_impact: bool = True
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Predict factual and counterfactual probabilities of climate change awareness using XGBoost.

    This function estimates how both direct and indirect effects of education influence
    the probability of being aware of climate change. A factual model is trained using
    observed data, while a counterfactual scenario simulates higher education levels
    and modified knowledge exposure.

    The function uses a 10-fold stratified cross-validation repeated under different random seeds,
    and integrates pre-estimated factual and counterfactual knowledge probabilities as additional
    model features. For each fold, an XGBoost classifier is fitted with optimal hyperparameters
    retrieved from prior tuning results, and both factual and counterfactual predictions are stored.

    Args:
        df_inuse (pd.DataFrame):
            Input dataset containing explanatory variables and the target variable
            `'Climate Change Awareness Dummy'`.
        factural_knowledge_probs (pd.DataFrame):
            DataFrame of factual knowledge prediction probabilities (mean across folds).
        counterfactual_knowledge_probs (pd.DataFrame):
            DataFrame of counterfactual knowledge prediction probabilities (mean across folds).
        direct_impact (bool, optional):
            If True, directly increases 'Education Year' by 1 and sets both
            literacy dummies ('Literate Education Dummy' and 'Illiterate Dummy') to 0
            to simulate the direct effect of education improvement. Default is True.
        indirect_impact (bool, optional):
            If True, replaces the factual knowledge probability feature with the
            counterfactual version to simulate the indirect (knowledge-mediated) effect. Default is True.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]:
            - **prob_matrix**: DataFrame of factual prediction probabilities
              (10-fold columns + mean column).
            - **prob_matrix_tide**: DataFrame of counterfactual prediction probabilities
              (10-fold columns + mean column).

    Notes:
        - Class imbalance is addressed using `scale_pos_weight` in XGBoost.
        - The model uses pre-optimized hyperparameters loaded from the prior tuning results file:
          `'MLD01e_Results/MLD01e_C11_AwarenessFactorInvestigation_v1.parquet'`.
        - Both output DataFrames have one row per observation, allowing sample-level analysis
          of factual–counterfactual changes in awareness probability.
    """
    # Extract target and features
    y = df_inuse['Climate Change Awareness Dummy'].astype(int)
    X = df_inuse.drop(columns=['Climate Change Awareness Dummy'])

    # Calculate class imbalance weight
    pos = y.sum()
    neg = len(y) - pos
    scale_pos_weight = (neg / pos) if pos > 0 else 1.0
    
    # Add factual knowledge probability as a feature
    X['Heard about Climate Change Probability'] = factural_knowledge_probs['mean'].to_list()
    
    # Load best hyperparameters from previous search
    cvres = pd.read_parquet('MLD01e_Results/MLD01e_C11_AwarenessFactorInvestigation_v1.parquet')
    params = cvres.sort_values('rank_test_score').iloc[0,10]

    # Initialize probability matrices
    prob_matrix = pd.DataFrame(np.zeros([X.shape[0], 10]))
    prob_matrix_tide = pd.DataFrame(np.zeros([X.shape[0], 10]))

    # Repeated stratified 10-fold cross-validation
    for epoch, random_seed in enumerate(range(42, 42*11, 42)):
        cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=random_seed)
        for fold, (train_idx, test_idx) in enumerate(cv.split(X, y), 1):
            X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
            y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
            # Ensure test columns match train columns
            X_test = X_test.reindex(columns=X_train.columns, fill_value=0)
            pos = y_train.sum()
            neg = len(y_train) - pos
            scale_pos_weight = (neg / pos) if pos > 0 else 1.0
            # Train XGBoost classifier
            clf = XGBClassifier(objective="binary:logistic",
                                eval_metric="logloss", tree_method="hist", 
                                random_state=random_seed, 
                                scale_pos_weight=scale_pos_weight, device = 'cuda',
                                **params)
            clf.fit(X_train, y_train)
            # Factual prediction
            prob_matrix.iloc[test_idx, epoch] = clf.predict_proba(X_test)[:, 1]
            # Counterfactual: increase education year, set literacy dummies to 0, update knowledge probability
            X_tide = X_test.copy()

            if direct_impact:
                X_tide['Education Year'] = X_tide['Education Year'] + 1
                X_tide['Literate Education Dummy'] = 0
                X_tide['Illiterate Dummy'] = 0

            if indirect_impact:
                X_tide['Heard about Climate Change Probability'] = counterfactual_knowledge_probs['mean'].iloc[test_idx].to_list()
            prob_matrix_tide.iloc[test_idx, epoch] = clf.predict_proba(X_tide)[:, 1]
        print(f'epoch: {epoch}, random_seed:{random_seed}')
    # Calculate mean probability across folds
    prob_matrix['mean'] = prob_matrix.mean(axis=1)
    prob_matrix_tide['mean'] = prob_matrix_tide.mean(axis=1)
    return prob_matrix, prob_matrix_tide

def predicting_counter_and_factual_action_based_xgboost(
    df_inuse: 'pd.DataFrame',
    factural_knowledge_probs: 'pd.DataFrame',
    counterfactual_knowledge_probs: 'pd.DataFrame',
    factural_awareness_probs: 'pd.DataFrame',
    counterfactual_awareness_probs: 'pd.DataFrame',
    action_type: str,
    direct_impact: bool = True,
    indirect_impact: bool = True
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Predict factual and counterfactual probabilities of taking a specific climate change
    adaptation action using XGBoost.

    The function estimates how education affects the probability of taking the chosen action
    through: (i) a direct channel (altering education-related covariates), and (ii) an indirect,
    knowledge/awareness-mediated channel (replacing the factual knowledge/awareness features with
    their counterfactual counterparts). Models are trained with repeated 10-fold stratified
    cross-validation under different random seeds, using best hyperparameters retrieved from a
    prior tuning run for the specified action.

    Args:
        df_inuse (pd.DataFrame):
            Feature matrix and the target action column. `action_type` must be a binary column
            in this DataFrame (1 = took the action, 0 = otherwise).
        factural_knowledge_probs (pd.DataFrame):
            Factual knowledge probabilities (e.g., a column `'mean'` aligned by row with df_inuse).
        counterfactual_knowledge_probs (pd.DataFrame):
            Counterfactual knowledge probabilities (same shape/row order; typically a `'mean'` column).
        factural_awareness_probs (pd.DataFrame):
            Factual awareness probabilities (e.g., `'mean'`).
        counterfactual_awareness_probs (pd.DataFrame):
            Counterfactual awareness probabilities (e.g., `'mean'`).
        action_type (str):
            The column name in `df_inuse` representing the action to predict (binary target).
        direct_impact (bool, optional):
            If True, simulate direct education effects by modifying education-related covariates
            (e.g., +1 year of education; set literacy dummies to 0) in the counterfactual data.
            Default: True.
        indirect_impact (bool, optional):
            If True, simulate indirect effects by replacing the factual knowledge/awareness
            probability features with their counterfactual versions. Default: True.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]:
            - prob_matrix:
                Factual prediction probabilities for each observation across folds
                (10 fold-wise columns) plus a `'mean'` column (average across folds).
            - prob_matrix_tide:
                Counterfactual prediction probabilities for each observation across folds
                (10 fold-wise columns) plus a `'mean'` column.

    Notes:
        - Class imbalance is handled via `scale_pos_weight` within XGBoost on each training split.
        - Hyperparameters are loaded from a prior model selection artifact tailored to `action_type`.
        - All probability inputs are expected to align 1:1 by row with `df_inuse`.
        - Outputs retain row order, enabling sample-level comparisons between factual and
          counterfactual action probabilities.
    """
    # Extract target and features
    y = df_inuse[action_type].astype(int)
    X = df_inuse.drop(columns=[action_type])

    # Calculate class imbalance weight
    pos = y.sum()
    neg = len(y) - pos
    scale_pos_weight = (neg / pos) if pos > 0 else 1.0
    
    # Add factual knowledge and awareness probabilities as features
    X['Heard about Climate Change Probability'] = factural_knowledge_probs['mean'].to_list()
    X['Climate Change Awareness Probability'] = factural_awareness_probs['mean'].to_list()
    
    # Dictionary mapping action types to their hyperparameter search result file
    action_address_dict = {
        'Soil and Water Conservation Measures in Past Dummy': 'MLD01e_Results/MLD01e_C21_ActionFactorInvestigation_SoilWaterConservationPast25_v1.parquet',
        'Risk Reduction Measurement in Past Dummy': 'MLD01e_Results/MLD01e_C31_ActionFactorInvestigation_RiskReductionPast25_v1.parquet',
        'Road Improvement in Past Dummy': 'MLD01e_Results/MLD01e_C41_ActionFactorInvestigation_RoadImprovementPast25_v1.parquet',
        'Community Participation in Past Dummy': 'MLD01e_Results/MLD01e_C51_ActionFactorInvestigation_CommunityPartipationPast25_v1.parquet'
    }
    # Load best hyperparameters for the given action type
    cvres = pd.read_parquet(action_address_dict.get(action_type))
    params = cvres.sort_values('rank_test_score').iloc[0,10]

    # Initialize probability matrices
    prob_matrix = pd.DataFrame(np.zeros([X.shape[0], 10]))
    prob_matrix_tide = pd.DataFrame(np.zeros([X.shape[0], 10]))

    # Repeated stratified 10-fold cross-validation
    for epoch, random_seed in enumerate(range(42, 42*11, 42)):
        cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=random_seed)
        for fold, (train_idx, test_idx) in enumerate(cv.split(X, y), 1):
            X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
            y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
            # Ensure test columns match train columns
            X_test = X_test.reindex(columns=X_train.columns, fill_value=0)
            pos = y_train.sum()
            neg = len(y_train) - pos
            scale_pos_weight = (neg / pos) if pos > 0 else 1.0
            # Train XGBoost classifier
            clf = XGBClassifier(objective="binary:logistic",
                                eval_metric="logloss", tree_method="hist", 
                                random_state=random_seed, 
                                scale_pos_weight=scale_pos_weight, device = 'cuda',
                                **params)
            clf.fit(X_train, y_train)
            # Factual prediction
            prob_matrix.iloc[test_idx, epoch] = clf.predict_proba(X_test)[:, 1]
            # Counterfactual: increase education year, set literacy dummies to 0, update knowledge and awareness probabilities
            X_tide = X_test.copy()

            if direct_impact:
                X_tide['Education Year'] = X_tide['Education Year'] + 1
                X_tide['Literate Education Dummy'] = 0
                X_tide['Illiterate Dummy'] = 0

            if indirect_impact:
                X_tide['Heard about Climate Change Probability'] = counterfactual_knowledge_probs['mean'].iloc[test_idx].to_list()
                X_tide['Climate Change Awareness Probability'] = counterfactual_awareness_probs['mean'].iloc[test_idx].to_list()
            prob_matrix_tide.iloc[test_idx, epoch] = clf.predict_proba(X_tide)[:, 1]
        print(f'epoch: {epoch}, random_seed:{random_seed}')
    # Calculate mean probability across folds
    prob_matrix['mean'] = prob_matrix.mean(axis=1)
    prob_matrix_tide['mean'] = prob_matrix_tide.mean(axis=1)
    return prob_matrix, prob_matrix_tide
