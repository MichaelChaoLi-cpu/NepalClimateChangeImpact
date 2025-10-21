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
