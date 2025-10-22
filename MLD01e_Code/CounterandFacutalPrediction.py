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
    counterfactual_knowledge_probs: 'pd.DataFrame'
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Perform counterfactual and factual prediction of climate change awareness using XGBoost.

    This function uses an XGBoost classifier to predict the probability of being aware of climate change (factual)
    and the probability under a counterfactual scenario where education year is increased by 1 and literacy dummies are set to 0.
    It adds factual and counterfactual knowledge probabilities as features, performs repeated stratified 10-fold cross-validation
    with different random seeds, and uses the best hyperparameters from a previous search. Returns probability matrices for both factual
    and counterfactual predictions, with mean probabilities across folds.

    Args:
        df_inuse (pd.DataFrame): Input DataFrame with features and the target column 'Climate Change Awareness Dummy'.
        factural_knowledge_probs (pd.DataFrame): DataFrame of factual knowledge probabilities.
        counterfactual_knowledge_probs (pd.DataFrame): DataFrame of counterfactual knowledge probabilities.
    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]:
            - prob_matrix: Factual prediction probabilities for each sample (mean across folds).
            - prob_matrix_tide: Counterfactual prediction probabilities for each sample (mean across folds).
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
            X_tide['Education Year'] = X_tide['Education Year'] + 1
            X_tide['Literate Education Dummy'] = 0
            X_tide['Illiterate Dummy'] = 0
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
    action_type: str
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Perform counterfactual and factual prediction of climate change adaptation actions using XGBoost.

    This function predicts the probability of taking a specific adaptation action (factual)
    and the probability under a counterfactual scenario where education year is increased by 1 and literacy dummies are set to 0.
    It adds factual and counterfactual knowledge and awareness probabilities as features, performs repeated stratified 10-fold cross-validation
    with different random seeds, and uses the best hyperparameters from a previous search for the specified action type.
    Returns probability matrices for both factual and counterfactual predictions, with mean probabilities across folds.

    Args:
        df_inuse (pd.DataFrame): Input DataFrame with features and the target action column.
        factural_knowledge_probs (pd.DataFrame): DataFrame of factual knowledge probabilities.
        counterfactual_knowledge_probs (pd.DataFrame): DataFrame of counterfactual knowledge probabilities.
        factural_awareness_probs (pd.DataFrame): DataFrame of factual awareness probabilities.
        counterfactual_awareness_probs (pd.DataFrame): DataFrame of counterfactual awareness probabilities.
        action_type (str): The column name of the action to predict.
    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]:
            - prob_matrix: Factual prediction probabilities for each sample (mean across folds).
            - prob_matrix_tide: Counterfactual prediction probabilities for each sample (mean across folds).
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
            X_tide['Education Year'] = X_tide['Education Year'] + 1
            X_tide['Literate Education Dummy'] = 0
            X_tide['Illiterate Dummy'] = 0
            X_tide['Heard about Climate Change Probability'] = counterfactual_knowledge_probs['mean'].iloc[test_idx].to_list()
            X_tide['Climate Change Awareness Probability'] = counterfactual_awareness_probs['mean'].iloc[test_idx].to_list()
            prob_matrix_tide.iloc[test_idx, epoch] = clf.predict_proba(X_tide)[:, 1]
        print(f'epoch: {epoch}, random_seed:{random_seed}')
    # Calculate mean probability across folds
    prob_matrix['mean'] = prob_matrix.mean(axis=1)
    prob_matrix_tide['mean'] = prob_matrix_tide.mean(axis=1)
    return prob_matrix, prob_matrix_tide
