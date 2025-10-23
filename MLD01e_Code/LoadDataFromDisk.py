import os
import pandas as pd

from glob import glob
from typing import Optional 

def load_data_from_disk() -> 'pd.DataFrame':
    """
    Loads and preprocesses household survey data from disk for the years 2016 and 2022.
    
    - Reads two Parquet files containing survey data for 2016 and 2022.
    - Adds a 'Year' column to each DataFrame.
    - Concatenates the data, drops columns with any missing values, and sets a multi-index.
    - Standardizes the 'EcoBelt' naming convention.
    - Creates dummy variables for EcoBelt, Province, main income sources, residence ownership, and residence infrastructure type.
    - Returns a cleaned and feature-engineered DataFrame ready for analysis.
    """
    # Read 2016 and 2022 data, add year column
    df_2016 = pd.read_parquet('Data/01_Napel2016.parquet')
    df_2016['Year'] = 2016
    df_2022 = pd.read_parquet('Data/01_Napel2022.parquet')
    df_2022['Year'] = 2022
    # Combine, drop columns with any missing values, set index
    df_all = pd.concat([df_2016, df_2022], axis = 0)
    df_all = df_all.dropna(axis=1, how="any")
    df_all = df_all.set_index(['PSU', 'HHLD'])
    # Standardize EcoBelt naming
    df_all["EcoBelt"] = df_all["EcoBelt"].str.replace('Tarai', 'Terai')
    
    # Create dummy variables for EcoBelt and Province
    eco_dummies = pd.get_dummies(df_all["EcoBelt"], prefix="EcoBelt").astype(int)
    df_all = pd.concat([df_all, eco_dummies], axis=1)

    prov_dummies = pd.get_dummies(df_all["Prov"], prefix="Prov").astype(int)
    df_all = pd.concat([df_all, prov_dummies], axis=1)

    # Create dummy variables for main income sources
    df_all['IncomeResAgri_dummy'] = (df_all[['IncomeS1', 'IncomeS2', 'IncomeS3']] == 1).any(axis=1).astype(int)
    df_all['IncomeResWage_dummy'] = (df_all[['IncomeS1', 'IncomeS2', 'IncomeS3']] == 2).any(axis=1).astype(int)
    df_all['IncomeResNonAgriBusi_dummy'] = (df_all[['IncomeS1', 'IncomeS2', 'IncomeS3']] == 3).any(axis=1).astype(int)
    df_all['IncomeResRemit_dummy'] = (df_all[['IncomeS1', 'IncomeS2', 'IncomeS3']] == 4).any(axis=1).astype(int)
    df_all['IncomeResOthers_dummy'] = (df_all[['IncomeS1', 'IncomeS2', 'IncomeS3']] == 5).any(axis=1).astype(int)

    # Create dummy variables for residence ownership
    df_all['ResidenceOwn_dummy'] = (df_all['Own_Resid'] == 1).astype(int)
    df_all['ResidenceRent_dummy'] = (df_all['Own_Resid'] == 2).astype(int)
    df_all['ResidenceInstitu_dummy'] = (df_all['Own_Resid'] == 3).astype(int)
    df_all['ResidenceOthers_dummy'] = (df_all['Own_Resid'] == 4).astype(int)

    # Create dummy variables for residence infrastructure type
    df_all['ResidInfraPerman_dummy'] = (df_all['Resid_Type'] == 1).astype(int)
    df_all['ResidInfraSemi_dummy'] = (df_all['Resid_Type'] == 2).astype(int)
    df_all['ResidInfraKachchi_dummy'] = (df_all['Resid_Type'] == 3).astype(int)
    df_all['ResidInfraOthers_dummy'] = (df_all['Resid_Type'] == 4).astype(int)
    
    return df_all

def read_all_probs_df_from_parquet(results_addr:str) -> dict:
    """
    Read all .parquet files in a directory into a dictionary of DataFrames.

    This function scans the specified directory for all .parquet files, reads each file into a pandas DataFrame,
    and stores them in a dictionary with keys based on the file names (without the .parquet extension).

    Args:
        results_addr (str): The directory path containing .parquet files.

    Returns:
        dict: A dictionary where keys are file names (without extension) and values are pandas DataFrames.
    """
    probs_dictionary = {}
    file_address = sorted(glob(os.path.join(results_addr, '*.parquet')))
    for file in file_address:
        key = os.path.basename(file).replace('.parquet', '')
        probs_dictionary[key] = pd.read_parquet(file)
    return probs_dictionary