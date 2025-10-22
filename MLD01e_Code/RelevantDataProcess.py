import pandas as pd
from typing import Optional

def make_data_for_knowledge_related_analysis(df_all: 'pd.DataFrame') -> 'pd.DataFrame':
    """
    Prepare a DataFrame for climate change knowledge-related analysis.

    This function selects relevant variables from the input household survey DataFrame, including demographics, location, assets, income sources, and other factors
    that may influence climate change knowledge and related behaviors. It then renames the columns to human-readable labels for clarity in analysis.

    Args:
        df_all (pd.DataFrame): The full household survey DataFrame containing all variables.

    Returns:
        pd.DataFrame: A DataFrame containing selected and renamed variables for knowledge-related analysis.
    """
    # Select relevant columns for knowledge-related analysis
    df_inuse = df_all[[
        # Demographics and education
        'HeardClimate_Dummy', 'Respon_Female', 'Respon_Age', 'LivingYear', 'Edu_Literal', 'Edu_Illiterate', 'Edu_year',
        'Female_Ratio', 'U18_Ratio', 'A65_Ratio', 'Edu12_Ratio', 'Literal_Ratio',
        # Location
        'EcoBelt_Hill', 'EcoBelt_Mountain', 'EcoBelt_Terai',
        'Prov_Bagmati', 'Prov_Koshi', 'Prov_Lumbini', 'Prov_Madhesh', 'Prov_Sudurpaschim', 'Prov_Gandaki', 'Prov_Karnali',
        # Residence and infrastructure
        'ResidenceOwn_dummy', 'ResidenceRent_dummy', 'ResidenceInstitu_dummy', 'ResidenceOthers_dummy',
        'ResidInfraPerman_dummy', 'ResidInfraSemi_dummy', 'ResidInfraKachchi_dummy', 'ResidInfraOthers_dummy',
        # Remittance and agriculture
        'Remittance_dummy', 'Have_AgriLand', 'HouseHead_AgriExpYear',
        # Assets
        'Radio_dummy', 'TV_dummy', 'PC_dummy', 'Net_dummy', 'Phone_dummy', 'Mobile_dummy', 'Motorbike_dummy', 'Car_dummy', 'Bike_dummy', 'OtherVehi_dummy', 'Refrige_dummy',
        # Memberships and support
        'SavingMembership', 'RegularSaving', 'OrgMembership', 'AgriSupport',
        # Distances
        'Dist_Road', 'Dist_HealthCenter', 'Dist_SecondarySchool', 'Dist_Market', 'Dist_AgriSupport',
        # Farm mechanization
        'FramMechan',
        # Income sources
        'IncomeResAgri_dummy', 'IncomeResWage_dummy', 'IncomeResNonAgriBusi_dummy', 'IncomeResRemit_dummy', 'IncomeResOthers_dummy',
        # Income
        'CropIncome', 'LivestockIncome', 'NonAgriIncome', 'BusiIncome', 'TotalIncome',
        # Survey year
        'Year'
    ]]
    # Map variable names to human-readable labels for clarity in analysis
    variname_readable = {'HeardClimate_Dummy':'Heard about Climate Change Dummy', 'Respon_Female':'Female Dummy', 
                     'Respon_Age':'Age', 'LivingYear':'Years Living in Community', 'Edu_UnderSLC':'Education under Secondary Certificate Dummy', 
                     'Edu_Certificate':'Education with Secondary Certificate Dummy', 'Edu_Bachelor':'Education with Bachelor Dummy', 
                     'Edu_Master':'Education with Master Dummy',  'Edu_PhD':'Education with PhD Dummy', 
                     'Edu_Literal':'Literate Education Dummy',  'Edu_Illiterate':'Illiterate Dummy', 'Edu_year':'Education Year',
                     'Female_Ratio':'Female Ratio in Household', 'U18_Ratio':'Member Under 18 Ratio', 'A65_Ratio':'Seniors Ratio',
                     'Edu12_Ratio':"Member with 12-Year Education or above Ratio", "Literal_Ratio": "Literate Member Ratio",
                     'EcoBelt_Hill': "EcoBelt Hill Dummy", 'EcoBelt_Mountain': "EcoBelt Mountain Dummy", 'EcoBelt_Terai': "EcoBelt Terai Dummy",
                     'Prov_Bagmati': "Province Bagmati Dummy", 'Prov_Koshi': "Province Koshi Dummy", 'Prov_Lumbini': "Province Lumbibi Dummy",
                     'Prov_Madhesh': "Province Madhesh Dummy", 'Prov_Sudurpaschim': "Province Sudurpaschim Dummy", 'Prov_Gandaki': "Province Gandaki Dummy",
                     'Prov_Karnali': "Province Karnali Dummy",
                     'ResidenceOwn_dummy': "Owned Residence Ownership Dummy", 'ResidenceRent_dummy': 'Rented Residence Ownership Dummy', 
                     'ResidenceInstitu_dummy': 'Institutional Residence Ownership Dummy', 'ResidenceOthers_dummy': 'Other-type Residence Ownership Dummy',
                     'ResidInfraPerman_dummy': 'Permanent Residence Dummy', 'ResidInfraSemi_dummy': 'Semi-Permanent Residence Dummy', 
                     'ResidInfraKachchi_dummy': "Kachchi Residence Dummy", 'ResidInfraOthers_dummy': 'Other Residence Infrastructure Dummy', # house
                     'Remittance_dummy' : "Have Remittance",
                     'Have_AgriLand': "Having Agricultural Land Dummy", 'HouseHead_AgriExpYear': "Household Head Agricultural Experience",
                     'Radio_dummy': "Having Radio Dummy", 'TV_dummy': "Having TV Dummy", 'PC_dummy': "Having Computer Dummy", 'Net_dummy': "Having Internet Dummy",
                     'Phone_dummy': "Having Telephone Dummy", 'Mobile_dummy': "Having Mobile Dummy", 'Motorbike_dummy': "Having Motorbike Dummy", 
                     'Car_dummy': "Having Car Dummy", 'Bike_dummy': "Having Bike Dummy", 'OtherVehi_dummy': "Having Other Vehicle Dummy", 
                     'Refrige_dummy':"Having Refrigator Dummy",
                     'SavingMembership': "Saving Membership Dummy", 'RegularSaving': 'Having Regular Saving Dummy', 
                     'OrgMembership': 'Having Organization Membership Dummy', 'AgriSupport':'Agricultural Supporting Dummy', 
                     'Dist_Road': 'Distance to Motorable Road', 'Dist_HealthCenter': "Distance to Health Center", 
                     'Dist_SecondarySchool': "Distance to Secondary School", 'Dist_Market':"Distance to Market", 'Dist_AgriSupport': 'Distance to Agricultural Center', 
                     'FramMechan':'Farm Mechanization Dummy',
                     'IncomeResAgri_dummy': "Agricultural Income Source Dummy", 'IncomeResWage_dummy': "Wage Income Source Dummy",
                     'IncomeResNonAgriBusi_dummy': "Non-Agricultural Business Income Source Dummy", 'IncomeResRemit_dummy': "Remittance Income Dummy",
                     'IncomeResOthers_dummy': "Others Income Source Dummy", 
                     'CropIncome': "Crop Income", 'LivestockIncome': "Livestock Income", 'NonAgriIncome': "Non-agricultural Income", 
                     'BusiIncome': "Business Income", 'TotalIncome': "Total Income",
                     'Year': "Survey Year"                    
                    }
    df_inuse.columns = df_inuse.columns.map(variname_readable)
    
    return df_inuse

def make_data_for_awareness_related_analysis(df_all: 'pd.DataFrame') -> 'pd.DataFrame':
    """
    Prepare a DataFrame for climate change awareness-related analysis.

    This function selects relevant variables from the input household survey DataFrame, including demographics, location, assets, income sources, disaster experiences, and other factors
    that may influence climate change awareness and related behaviors. It then renames the columns to human-readable labels for clarity in analysis.

    Args:
        df_all (pd.DataFrame): The full household survey DataFrame containing all variables.
    Returns:
        pd.DataFrame: A DataFrame containing selected and renamed variables for awareness-related analysis.
    """
    # Select relevant columns for awareness-related analysis
    # Includes demographics, location, assets, income, disaster experiences, and more
    df_inuse = df_all[['ClimateChanged_Dummy',  
                    'Respon_Female', 'Respon_Age', 'LivingYear', 'Edu_Literal', 'Edu_Illiterate', 'Edu_year', # S01
                    'Female_Ratio', 'U18_Ratio', 'A65_Ratio', 'Edu12_Ratio', 'Literal_Ratio', # S02-1
                    'EcoBelt_Hill', 'EcoBelt_Mountain', 'EcoBelt_Terai', 
                    'Prov_Bagmati', 'Prov_Koshi', 'Prov_Lumbini', 'Prov_Madhesh', 'Prov_Sudurpaschim',
                    'Prov_Gandaki', 'Prov_Karnali', # location     
                    'ResidenceOwn_dummy', 'ResidenceRent_dummy', 'ResidenceInstitu_dummy', 'ResidenceOthers_dummy',
                    'ResidInfraPerman_dummy', 'ResidInfraSemi_dummy', 'ResidInfraKachchi_dummy', 'ResidInfraOthers_dummy', # house
                    'Remittance_dummy', 
                    'Have_AgriLand', 'HouseHead_AgriExpYear',
                    'Radio_dummy', 'TV_dummy', 'PC_dummy', 'Net_dummy', 'Phone_dummy',
                    'Mobile_dummy', 'Motorbike_dummy', 'Car_dummy', 'Bike_dummy', 'OtherVehi_dummy', 'Refrige_dummy',
                    'SavingMembership', 'RegularSaving', 'OrgMembership', 'AgriSupport', 
                    'Dist_Road', 'Dist_HealthCenter', 'Dist_SecondarySchool', 'Dist_Market', 'Dist_AgriSupport', 
                    'FramMechan',
                    'IncomeResAgri_dummy', 'IncomeResWage_dummy', 'IncomeResNonAgriBusi_dummy', 'IncomeResRemit_dummy',
                    'IncomeResOthers_dummy', 
                    'CropIncome', 'LivestockIncome', 'NonAgriIncome', 'BusiIncome', 'TotalIncome',
                    'Year',
                    
                    # Disaster experiences
                    'ExpDummyDR', 'ExpDummyFF', 'ExpDummyFS', 'ExpDummyFL', 'ExpDummyIN', 'ExpDummyWS', 
                    'ExpDummyTS', 'ExpDummyHS', 'ExpDummyHR', 'ExpDummySR', 'ExpDummySE', 'ExpDummyLS', 
                    'ExpDummySS', 'ExpDummyAV', 'ExpDummyGLOF', 'ExpDummyHW', 'ExpDummyCW', 'ExpDummyDI', 
                    'ExpDummyOT',
                    
                    # DisasterFoodShortage
                    'DisasterFoodShortage_DummyDR', 'DisasterFoodShortage_DummyFF', 'DisasterFoodShortage_DummyFS', 
                    'DisasterFoodShortage_DummyFL', 'DisasterFoodShortage_DummyIN', 'DisasterFoodShortage_DummyWS', 
                    'DisasterFoodShortage_DummyTS', 'DisasterFoodShortage_DummyHS', 'DisasterFoodShortage_DummyHR', 
                    'DisasterFoodShortage_DummySR', 'DisasterFoodShortage_DummySE', 'DisasterFoodShortage_DummyLS', 
                    'DisasterFoodShortage_DummySS', 'DisasterFoodShortage_DummyAV', 'DisasterFoodShortage_DummyGLOF', 
                    'DisasterFoodShortage_DummyHW', 'DisasterFoodShortage_DummyCW', 'DisasterFoodShortage_DummyDI', 
                    'DisasterFoodShortage_DummyOT', 'DisasterDie_DummyDR', 
                    
                    # DisasterDie
                    'DisasterDie_DummyFF', 'DisasterDie_DummyFS', 'DisasterDie_DummyFL', 'DisasterDie_DummyIN', 
                    'DisasterDie_DummyWS', 'DisasterDie_DummyTS', 'DisasterDie_DummyHS', 'DisasterDie_DummyHR', 
                    'DisasterDie_DummySR', 'DisasterDie_DummySE', 'DisasterDie_DummyLS', 'DisasterDie_DummySS', 
                    'DisasterDie_DummyAV', 'DisasterDie_DummyGLOF', 'DisasterDie_DummyHW', 'DisasterDie_DummyCW', 
                    'DisasterDie_DummyDI', 'DisasterDie_DummyOT', 
                    
                    # DisasterMoneyLoss
                    'DisasterMoneyLoss_DummyDR', 'DisasterMoneyLoss_DummyFF', 'DisasterMoneyLoss_DummyFS', 
                    'DisasterMoneyLoss_DummyFL', 'DisasterMoneyLoss_DummyIN', 'DisasterMoneyLoss_DummyWS', 
                    'DisasterMoneyLoss_DummyTS', 'DisasterMoneyLoss_DummyHS', 'DisasterMoneyLoss_DummyHR', 
                    'DisasterMoneyLoss_DummySR', 'DisasterMoneyLoss_DummySE', 'DisasterMoneyLoss_DummyLS', 
                    'DisasterMoneyLoss_DummySS', 'DisasterMoneyLoss_DummyAV', 'DisasterMoneyLoss_DummyGLOF',
                    'DisasterMoneyLoss_DummyHW', 'DisasterMoneyLoss_DummyCW', 'DisasterMoneyLoss_DummyDI', 
                    'DisasterMoneyLoss_DummyOT', 
                    
    ]]
    
    # Map variable names to human-readable labels for clarity in analysis
    variname_readable = {'ClimateChanged_Dummy':'Climate Change Awareness Dummy',
                     'Heard about Climate Change Probability':'Heard about Climate Change Probability', 'Respon_Female':'Female Dummy', 
                     'Respon_Age':'Age', 'LivingYear':'Years Living in Community', 'Edu_UnderSLC':'Education under Secondary Certificate Dummy', 
                     'Edu_Certificate':'Education with Secondary Certificate Dummy', 'Edu_Bachelor':'Education with Bachelor Dummy', 
                     'Edu_Master':'Education with Master Dummy',  'Edu_PhD':'Education with PhD Dummy', 
                     'Edu_Literal':'Literate Education Dummy',  'Edu_Illiterate':'Illiterate Dummy', 'Edu_year':'Education Year',
                     'Female_Ratio':'Female Ratio in Household', 'U18_Ratio':'Member Under 18 Ratio', 'A65_Ratio':'Seniors Ratio',
                     'Edu12_Ratio':"Member with 12-Year Education or above Ratio", "Literal_Ratio": "Literate Member Ratio",
                     'EcoBelt_Hill': "EcoBelt Hill Dummy", 'EcoBelt_Mountain': "EcoBelt Mountain Dummy", 'EcoBelt_Terai': "EcoBelt Terai Dummy",
                     'Prov_Bagmati': "Province Bagmati Dummy", 'Prov_Koshi': "Province Koshi Dummy", 'Prov_Lumbini': "Province Lumbibi Dummy",
                     'Prov_Madhesh': "Province Madhesh Dummy", 'Prov_Sudurpaschim': "Province Sudurpaschim Dummy", 'Prov_Gandaki': "Province Gandaki Dummy",
                     'Prov_Karnali': "Province Karnali Dummy",
                     'ResidenceOwn_dummy': "Owned Residence Ownership Dummy", 'ResidenceRent_dummy': 'Rented Residence Ownership Dummy', 
                     'ResidenceInstitu_dummy': 'Institutional Residence Ownership Dummy', 'ResidenceOthers_dummy': 'Other-type Residence Ownership Dummy',
                     'ResidInfraPerman_dummy': 'Permanent Residence Dummy', 'ResidInfraSemi_dummy': 'Semi-Permanent Residence Dummy', 
                     'ResidInfraKachchi_dummy': "Kachchi Residence Dummy", 'ResidInfraOthers_dummy': 'Other Residence Infrastructure Dummy', # house
                     'Remittance_dummy' : "Have Remittance",
                     'Have_AgriLand': "Having Agricultural Land Dummy", 'HouseHead_AgriExpYear': "Household Head Agricultural Experience",
                     'Radio_dummy': "Having Radio Dummy", 'TV_dummy': "Having TV Dummy", 'PC_dummy': "Having Computer Dummy", 'Net_dummy': "Having Internet Dummy",
                     'Phone_dummy': "Having Telephone Dummy", 'Mobile_dummy': "Having Mobile Dummy", 'Motorbike_dummy': "Having Motorbike Dummy", 
                     'Car_dummy': "Having Car Dummy", 'Bike_dummy': "Having Bike Dummy", 'OtherVehi_dummy': "Having Other Vehicle Dummy", 
                     'Refrige_dummy':"Having Refrigator Dummy",
                     'SavingMembership': "Saving Membership Dummy", 'RegularSaving': 'Having Regular Saving Dummy', 
                     'OrgMembership': 'Having Organization Membership Dummy', 'AgriSupport':'Agricultural Supporting Dummy', 
                     'Dist_Road': 'Distance to Motorable Road', 'Dist_HealthCenter': "Distance to Health Center", 
                     'Dist_SecondarySchool': "Distance to Secondary School", 'Dist_Market':"Distance to Market", 'Dist_AgriSupport': 'Distance to Agricultural Center', 
                     'FramMechan':'Farm Mechanization Dummy',
                     'IncomeResAgri_dummy': "Agricultural Income Source Dummy", 'IncomeResWage_dummy': "Wage Income Source Dummy",
                     'IncomeResNonAgriBusi_dummy': "Non-Agricultural Business Income Source Dummy", 'IncomeResRemit_dummy': "Remittance Income Dummy",
                     'IncomeResOthers_dummy': "Others Income Source Dummy", 
                     'CropIncome': "Crop Income", 'LivestockIncome': "Livestock Income", 'NonAgriIncome': "Non-agricultural Income", 
                     'BusiIncome': "Business Income", 'TotalIncome': "Total Income",
                     'Year': "Survey Year"                    
                    }
    variname_readable.update({
        # Awareness sources
        'ClimateInfo_Radio': "Heard Climate Info from Radio",
        'ClimateInfo_Telev': "Heard Climate Info from Television",
        'ClimateInfo_News ': "Heard Climate Info from Newspaper",
        'ClimateInfo_Aware': "Heard Climate Info from Awareness Program",
        'ClimateInfo_Local': "Heard Climate Info from Local Government",
        'ClimateInfo_Neigh': "Heard Climate Info from Neighbors",
        'ClimateInfo_Famil': "Heard Climate Info from Family",
        'ClimateInfo_Other': "Heard Climate Info from Other Sources",

        # Disaster experiences
        'ExpDummyDR': "Experienced Drought",
        'ExpDummyFF': "Experienced Flash Flood",
        'ExpDummyFS': "Experienced Forest Fire",
        'ExpDummyFL': "Experienced Flood",
        'ExpDummyIN': "Experienced Insect Infestation",
        'ExpDummyWS': "Experienced Windstorm",
        'ExpDummyTS': "Experienced Thunderstorm",
        'ExpDummyHS': "Experienced Hailstorm",
        'ExpDummyHR': "Experienced Heavy Rain",
        'ExpDummySR': "Experienced Snowfall/Rain",
        'ExpDummySE': "Experienced Earthquake",
        'ExpDummyLS': "Experienced Landslide",
        'ExpDummySS': "Experienced Snowstorm",
        'ExpDummyAV': "Experienced Avalanche",
        'ExpDummyGLOF': "Experienced Glacial Lake Outburst Flood",
        'ExpDummyHW': "Experienced Heat Wave",
        'ExpDummyCW': "Experienced Cold Wave",
        'ExpDummyDI': "Experienced Disease Outbreak",
        'ExpDummyOT': "Experienced Other Disaster",

        # Disaster Food Shortage
        'DisasterFoodShortage_DummyDR': "Food Shortage due to Drought",
        'DisasterFoodShortage_DummyFF': "Food Shortage due to Flash Flood",
        'DisasterFoodShortage_DummyFS': "Food Shortage due to Forest Fire",
        'DisasterFoodShortage_DummyFL': "Food Shortage due to Flood",
        'DisasterFoodShortage_DummyIN': "Food Shortage due to Insect Infestation",
        'DisasterFoodShortage_DummyWS': "Food Shortage due to Windstorm",
        'DisasterFoodShortage_DummyTS': "Food Shortage due to Thunderstorm",
        'DisasterFoodShortage_DummyHS': "Food Shortage due to Hailstorm",
        'DisasterFoodShortage_DummyHR': "Food Shortage due to Heavy Rain",
        'DisasterFoodShortage_DummySR': "Food Shortage due to Snowfall/Rain",
        'DisasterFoodShortage_DummySE': "Food Shortage due to Earthquake",
        'DisasterFoodShortage_DummyLS': "Food Shortage due to Landslide",
        'DisasterFoodShortage_DummySS': "Food Shortage due to Snowstorm",
        'DisasterFoodShortage_DummyAV': "Food Shortage due to Avalanche",
        'DisasterFoodShortage_DummyGLOF': "Food Shortage due to GLOF",
        'DisasterFoodShortage_DummyHW': "Food Shortage due to Heat Wave",
        'DisasterFoodShortage_DummyCW': "Food Shortage due to Cold Wave",
        'DisasterFoodShortage_DummyDI': "Food Shortage due to Disease Outbreak",
        'DisasterFoodShortage_DummyOT': "Food Shortage due to Other Disaster",
        'DisasterDie_DummyDR': "Death due to Drought",

        # Disaster Die
        'DisasterDie_DummyFF': "Death due to Flash Flood",
        'DisasterDie_DummyFS': "Death due to Forest Fire",
        'DisasterDie_DummyFL': "Death due to Flood",
        'DisasterDie_DummyIN': "Death due to Insect Infestation",
        'DisasterDie_DummyWS': "Death due to Windstorm",
        'DisasterDie_DummyTS': "Death due to Thunderstorm",
        'DisasterDie_DummyHS': "Death due to Hailstorm",
        'DisasterDie_DummyHR': "Death due to Heavy Rain",
        'DisasterDie_DummySR': "Death due to Snowfall/Rain",
        'DisasterDie_DummySE': "Death due to Earthquake",
        'DisasterDie_DummyLS': "Death due to Landslide",
        'DisasterDie_DummySS': "Death due to Snowstorm",
        'DisasterDie_DummyAV': "Death due to Avalanche",
        'DisasterDie_DummyGLOF': "Death due to GLOF",
        'DisasterDie_DummyHW': "Death due to Heat Wave",
        'DisasterDie_DummyCW': "Death due to Cold Wave",
        'DisasterDie_DummyDI': "Death due to Disease Outbreak",
        'DisasterDie_DummyOT': "Death due to Other Disaster",

        # Disaster Money Loss
        'DisasterMoneyLoss_DummyDR': "Money Loss due to Drought",
        'DisasterMoneyLoss_DummyFF': "Money Loss due to Flash Flood",
        'DisasterMoneyLoss_DummyFS': "Money Loss due to Forest Fire",
        'DisasterMoneyLoss_DummyFL': "Money Loss due to Flood",
        'DisasterMoneyLoss_DummyIN': "Money Loss due to Insect Infestation",
        'DisasterMoneyLoss_DummyWS': "Money Loss due to Windstorm",
        'DisasterMoneyLoss_DummyTS': "Money Loss due to Thunderstorm",
        'DisasterMoneyLoss_DummyHS': "Money Loss due to Hailstorm",
        'DisasterMoneyLoss_DummyHR': "Money Loss due to Heavy Rain",
        'DisasterMoneyLoss_DummySR': "Money Loss due to Snowfall/Rain",
        'DisasterMoneyLoss_DummySE': "Money Loss due to Earthquake",
        'DisasterMoneyLoss_DummyLS': "Money Loss due to Landslide",
        'DisasterMoneyLoss_DummySS': "Money Loss due to Snowstorm",
        'DisasterMoneyLoss_DummyAV': "Money Loss due to Avalanche",
        'DisasterMoneyLoss_DummyGLOF': "Money Loss due to GLOF",
        'DisasterMoneyLoss_DummyHW': "Money Loss due to Heat Wave",
        'DisasterMoneyLoss_DummyCW': "Money Loss due to Cold Wave",
        'DisasterMoneyLoss_DummyDI': "Money Loss due to Disease Outbreak",
        'DisasterMoneyLoss_DummyOT': "Money Loss due to Other Disaster",
    })
    df_inuse.columns = df_inuse.columns.map(variname_readable)
    
    return df_inuse

def make_data_for_action_related_analysis(
    df_all: 'pd.DataFrame',
    action_variable: Optional[str] = 'Soil and Water Conservation Measures in Past Dummy'
    ) -> 'pd.DataFrame':
    """
    Prepare a DataFrame for climate change action-related analysis.

    This function selects relevant variables from the input household survey DataFrame, including the specified action variable,
    demographics, location, assets, income sources, disaster experiences, and other factors that may influence climate change adaptation actions.
    It then renames the columns to human-readable labels for clarity in analysis.

    Args:
        df_all (pd.DataFrame): The full household survey DataFrame containing all variables.
        action_variable (str, optional): The action variable to analyze. Defaults to 'Soil and Water Conservation Measures in Past Dummy'.
    Returns:
        pd.DataFrame: A DataFrame containing selected and renamed variables for action-related analysis.
    """
    # Map action variable names to their corresponding column names in the DataFrame
    action_variable_dict = {
        'Soil and Water Conservation Measures in Past Dummy':"SoilWaterConservationPast25",
        'Risk Reduction Measurement in Past Dummy':'RiskReductionPast25',
        'Road Improvement in Past Dummy':'RoadImprovementPast25',
        'Community Participation in Past Dummy':'CommunityPartipationPast25'
    }
    # Ensure action_variable is valid
    if action_variable not in action_variable_dict:
        raise ValueError(f"action_variable must be one of: {list(action_variable_dict.keys())}")
    # Select relevant columns for action-related analysis
    # Includes the action variable, demographics, location, assets, income, disaster experiences, and more
    df_inuse = df_all[[action_variable_dict.get(action_variable),  
                    'Respon_Female', 'Respon_Age', 'LivingYear', 'Edu_Literal', 'Edu_Illiterate', 'Edu_year', # S01
                    'Female_Ratio', 'U18_Ratio', 'A65_Ratio', 'Edu12_Ratio', 'Literal_Ratio', # S02-1
                    'EcoBelt_Hill', 'EcoBelt_Mountain', 'EcoBelt_Terai', 
                    'Prov_Bagmati', 'Prov_Koshi', 'Prov_Lumbini', 'Prov_Madhesh', 'Prov_Sudurpaschim',
                    'Prov_Gandaki', 'Prov_Karnali', # location     
                    'ResidenceOwn_dummy', 'ResidenceRent_dummy', 'ResidenceInstitu_dummy', 'ResidenceOthers_dummy',
                    'ResidInfraPerman_dummy', 'ResidInfraSemi_dummy', 'ResidInfraKachchi_dummy', 'ResidInfraOthers_dummy', # house
                    'Remittance_dummy', 
                    'Have_AgriLand', 'HouseHead_AgriExpYear',
                    'Radio_dummy', 'TV_dummy', 'PC_dummy', 'Net_dummy', 'Phone_dummy',
                    'Mobile_dummy', 'Motorbike_dummy', 'Car_dummy', 'Bike_dummy', 'OtherVehi_dummy', 'Refrige_dummy',
                    'SavingMembership', 'RegularSaving', 'OrgMembership', 'AgriSupport', 
                    'Dist_Road', 'Dist_HealthCenter', 'Dist_SecondarySchool', 'Dist_Market', 'Dist_AgriSupport', 
                    'FramMechan',
                    'IncomeResAgri_dummy', 'IncomeResWage_dummy', 'IncomeResNonAgriBusi_dummy', 'IncomeResRemit_dummy',
                    'IncomeResOthers_dummy', 
                    'CropIncome', 'LivestockIncome', 'NonAgriIncome', 'BusiIncome', 'TotalIncome',
                    'Year',
                    
                    # Disaster experiences
                    'ExpDummyDR', 'ExpDummyFF', 'ExpDummyFS', 'ExpDummyFL', 'ExpDummyIN', 'ExpDummyWS', 
                    'ExpDummyTS', 'ExpDummyHS', 'ExpDummyHR', 'ExpDummySR', 'ExpDummySE', 'ExpDummyLS', 
                    'ExpDummySS', 'ExpDummyAV', 'ExpDummyGLOF', 'ExpDummyHW', 'ExpDummyCW', 'ExpDummyDI', 
                    'ExpDummyOT',
                    
                    # DisasterFoodShortage
                    'DisasterFoodShortage_DummyDR', 'DisasterFoodShortage_DummyFF', 'DisasterFoodShortage_DummyFS', 
                    'DisasterFoodShortage_DummyFL', 'DisasterFoodShortage_DummyIN', 'DisasterFoodShortage_DummyWS', 
                    'DisasterFoodShortage_DummyTS', 'DisasterFoodShortage_DummyHS', 'DisasterFoodShortage_DummyHR', 
                    'DisasterFoodShortage_DummySR', 'DisasterFoodShortage_DummySE', 'DisasterFoodShortage_DummyLS', 
                    'DisasterFoodShortage_DummySS', 'DisasterFoodShortage_DummyAV', 'DisasterFoodShortage_DummyGLOF', 
                    'DisasterFoodShortage_DummyHW', 'DisasterFoodShortage_DummyCW', 'DisasterFoodShortage_DummyDI', 
                    'DisasterFoodShortage_DummyOT', 'DisasterDie_DummyDR', 
                    
                    # DisasterDie
                    'DisasterDie_DummyFF', 'DisasterDie_DummyFS', 'DisasterDie_DummyFL', 'DisasterDie_DummyIN', 
                    'DisasterDie_DummyWS', 'DisasterDie_DummyTS', 'DisasterDie_DummyHS', 'DisasterDie_DummyHR', 
                    'DisasterDie_DummySR', 'DisasterDie_DummySE', 'DisasterDie_DummyLS', 'DisasterDie_DummySS', 
                    'DisasterDie_DummyAV', 'DisasterDie_DummyGLOF', 'DisasterDie_DummyHW', 'DisasterDie_DummyCW', 
                    'DisasterDie_DummyDI', 'DisasterDie_DummyOT', 
                    
                    # DisasterMoneyLoss
                    'DisasterMoneyLoss_DummyDR', 'DisasterMoneyLoss_DummyFF', 'DisasterMoneyLoss_DummyFS', 
                    'DisasterMoneyLoss_DummyFL', 'DisasterMoneyLoss_DummyIN', 'DisasterMoneyLoss_DummyWS', 
                    'DisasterMoneyLoss_DummyTS', 'DisasterMoneyLoss_DummyHS', 'DisasterMoneyLoss_DummyHR', 
                    'DisasterMoneyLoss_DummySR', 'DisasterMoneyLoss_DummySE', 'DisasterMoneyLoss_DummyLS', 
                    'DisasterMoneyLoss_DummySS', 'DisasterMoneyLoss_DummyAV', 'DisasterMoneyLoss_DummyGLOF',
                    'DisasterMoneyLoss_DummyHW', 'DisasterMoneyLoss_DummyCW', 'DisasterMoneyLoss_DummyDI', 
                    'DisasterMoneyLoss_DummyOT', 
                    
    ]]
    # Map variable names to human-readable labels for clarity in analysis
    variname_readable = {action_variable_dict.get(action_variable):action_variable,
                     'Heard about Climate Change Probability':'Heard about Climate Change Probability', 'Respon_Female':'Female Dummy', 
                     'Respon_Age':'Age', 'LivingYear':'Years Living in Community', 'Edu_UnderSLC':'Education under Secondary Certificate Dummy', 
                     'Edu_Certificate':'Education with Secondary Certificate Dummy', 'Edu_Bachelor':'Education with Bachelor Dummy', 
                     'Edu_Master':'Education with Master Dummy',  'Edu_PhD':'Education with PhD Dummy', 
                     'Edu_Literal':'Literate Education Dummy',  'Edu_Illiterate':'Illiterate Dummy', 'Edu_year':'Education Year',
                     'Female_Ratio':'Female Ratio in Household', 'U18_Ratio':'Member Under 18 Ratio', 'A65_Ratio':'Seniors Ratio',
                     'Edu12_Ratio':"Member with 12-Year Education or above Ratio", "Literal_Ratio": "Literate Member Ratio",
                     'EcoBelt_Hill': "EcoBelt Hill Dummy", 'EcoBelt_Mountain': "EcoBelt Mountain Dummy", 'EcoBelt_Terai': "EcoBelt Terai Dummy",
                     'Prov_Bagmati': "Province Bagmati Dummy", 'Prov_Koshi': "Province Koshi Dummy", 'Prov_Lumbini': "Province Lumbibi Dummy",
                     'Prov_Madhesh': "Province Madhesh Dummy", 'Prov_Sudurpaschim': "Province Sudurpaschim Dummy", 'Prov_Gandaki': "Province Gandaki Dummy",
                     'Prov_Karnali': "Province Karnali Dummy",
                     'ResidenceOwn_dummy': "Owned Residence Ownership Dummy", 'ResidenceRent_dummy': 'Rented Residence Ownership Dummy', 
                     'ResidenceInstitu_dummy': 'Institutional Residence Ownership Dummy', 'ResidenceOthers_dummy': 'Other-type Residence Ownership Dummy',
                     'ResidInfraPerman_dummy': 'Permanent Residence Dummy', 'ResidInfraSemi_dummy': 'Semi-Permanent Residence Dummy', 
                     'ResidInfraKachchi_dummy': "Kachchi Residence Dummy", 'ResidInfraOthers_dummy': 'Other Residence Infrastructure Dummy', # house
                     'Remittance_dummy' : "Have Remittance",
                     'Have_AgriLand': "Having Agricultural Land Dummy", 'HouseHead_AgriExpYear': "Household Head Agricultural Experience",
                     'Radio_dummy': "Having Radio Dummy", 'TV_dummy': "Having TV Dummy", 'PC_dummy': "Having Computer Dummy", 'Net_dummy': "Having Internet Dummy",
                     'Phone_dummy': "Having Telephone Dummy", 'Mobile_dummy': "Having Mobile Dummy", 'Motorbike_dummy': "Having Motorbike Dummy", 
                     'Car_dummy': "Having Car Dummy", 'Bike_dummy': "Having Bike Dummy", 'OtherVehi_dummy': "Having Other Vehicle Dummy", 
                     'Refrige_dummy':"Having Refrigator Dummy",
                     'SavingMembership': "Saving Membership Dummy", 'RegularSaving': 'Having Regular Saving Dummy', 
                     'OrgMembership': 'Having Organization Membership Dummy', 'AgriSupport':'Agricultural Supporting Dummy', 
                     'Dist_Road': 'Distance to Motorable Road', 'Dist_HealthCenter': "Distance to Health Center", 
                     'Dist_SecondarySchool': "Distance to Secondary School", 'Dist_Market':"Distance to Market", 'Dist_AgriSupport': 'Distance to Agricultural Center', 
                     'FramMechan':'Farm Mechanization Dummy',
                     'IncomeResAgri_dummy': "Agricultural Income Source Dummy", 'IncomeResWage_dummy': "Wage Income Source Dummy",
                     'IncomeResNonAgriBusi_dummy': "Non-Agricultural Business Income Source Dummy", 'IncomeResRemit_dummy': "Remittance Income Dummy",
                     'IncomeResOthers_dummy': "Others Income Source Dummy", 
                     'CropIncome': "Crop Income", 'LivestockIncome': "Livestock Income", 'NonAgriIncome': "Non-agricultural Income", 
                     'BusiIncome': "Business Income", 'TotalIncome': "Total Income",
                     'Year': "Survey Year"                    
                    }
    variname_readable.update({
        # Awareness sources
        'ClimateInfo_Radio': "Heard Climate Info from Radio",
        'ClimateInfo_Telev': "Heard Climate Info from Television",
        'ClimateInfo_News ': "Heard Climate Info from Newspaper",
        'ClimateInfo_Aware': "Heard Climate Info from Awareness Program",
        'ClimateInfo_Local': "Heard Climate Info from Local Government",
        'ClimateInfo_Neigh': "Heard Climate Info from Neighbors",
        'ClimateInfo_Famil': "Heard Climate Info from Family",
        'ClimateInfo_Other': "Heard Climate Info from Other Sources",

        # Disaster experiences
        'ExpDummyDR': "Experienced Drought",
        'ExpDummyFF': "Experienced Flash Flood",
        'ExpDummyFS': "Experienced Forest Fire",
        'ExpDummyFL': "Experienced Flood",
        'ExpDummyIN': "Experienced Insect Infestation",
        'ExpDummyWS': "Experienced Windstorm",
        'ExpDummyTS': "Experienced Thunderstorm",
        'ExpDummyHS': "Experienced Hailstorm",
        'ExpDummyHR': "Experienced Heavy Rain",
        'ExpDummySR': "Experienced Snowfall/Rain",
        'ExpDummySE': "Experienced Earthquake",
        'ExpDummyLS': "Experienced Landslide",
        'ExpDummySS': "Experienced Snowstorm",
        'ExpDummyAV': "Experienced Avalanche",
        'ExpDummyGLOF': "Experienced Glacial Lake Outburst Flood",
        'ExpDummyHW': "Experienced Heat Wave",
        'ExpDummyCW': "Experienced Cold Wave",
        'ExpDummyDI': "Experienced Disease Outbreak",
        'ExpDummyOT': "Experienced Other Disaster",

        # Disaster Food Shortage
        'DisasterFoodShortage_DummyDR': "Food Shortage due to Drought",
        'DisasterFoodShortage_DummyFF': "Food Shortage due to Flash Flood",
        'DisasterFoodShortage_DummyFS': "Food Shortage due to Forest Fire",
        'DisasterFoodShortage_DummyFL': "Food Shortage due to Flood",
        'DisasterFoodShortage_DummyIN': "Food Shortage due to Insect Infestation",
        'DisasterFoodShortage_DummyWS': "Food Shortage due to Windstorm",
        'DisasterFoodShortage_DummyTS': "Food Shortage due to Thunderstorm",
        'DisasterFoodShortage_DummyHS': "Food Shortage due to Hailstorm",
        'DisasterFoodShortage_DummyHR': "Food Shortage due to Heavy Rain",
        'DisasterFoodShortage_DummySR': "Food Shortage due to Snowfall/Rain",
        'DisasterFoodShortage_DummySE': "Food Shortage due to Earthquake",
        'DisasterFoodShortage_DummyLS': "Food Shortage due to Landslide",
        'DisasterFoodShortage_DummySS': "Food Shortage due to Snowstorm",
        'DisasterFoodShortage_DummyAV': "Food Shortage due to Avalanche",
        'DisasterFoodShortage_DummyGLOF': "Food Shortage due to GLOF",
        'DisasterFoodShortage_DummyHW': "Food Shortage due to Heat Wave",
        'DisasterFoodShortage_DummyCW': "Food Shortage due to Cold Wave",
        'DisasterFoodShortage_DummyDI': "Food Shortage due to Disease Outbreak",
        'DisasterFoodShortage_DummyOT': "Food Shortage due to Other Disaster",
        'DisasterDie_DummyDR': "Death due to Drought",

        # Disaster Die
        'DisasterDie_DummyFF': "Death due to Flash Flood",
        'DisasterDie_DummyFS': "Death due to Forest Fire",
        'DisasterDie_DummyFL': "Death due to Flood",
        'DisasterDie_DummyIN': "Death due to Insect Infestation",
        'DisasterDie_DummyWS': "Death due to Windstorm",
        'DisasterDie_DummyTS': "Death due to Thunderstorm",
        'DisasterDie_DummyHS': "Death due to Hailstorm",
        'DisasterDie_DummyHR': "Death due to Heavy Rain",
        'DisasterDie_DummySR': "Death due to Snowfall/Rain",
        'DisasterDie_DummySE': "Death due to Earthquake",
        'DisasterDie_DummyLS': "Death due to Landslide",
        'DisasterDie_DummySS': "Death due to Snowstorm",
        'DisasterDie_DummyAV': "Death due to Avalanche",
        'DisasterDie_DummyGLOF': "Death due to GLOF",
        'DisasterDie_DummyHW': "Death due to Heat Wave",
        'DisasterDie_DummyCW': "Death due to Cold Wave",
        'DisasterDie_DummyDI': "Death due to Disease Outbreak",
        'DisasterDie_DummyOT': "Death due to Other Disaster",

        # Disaster Money Loss
        'DisasterMoneyLoss_DummyDR': "Money Loss due to Drought",
        'DisasterMoneyLoss_DummyFF': "Money Loss due to Flash Flood",
        'DisasterMoneyLoss_DummyFS': "Money Loss due to Forest Fire",
        'DisasterMoneyLoss_DummyFL': "Money Loss due to Flood",
        'DisasterMoneyLoss_DummyIN': "Money Loss due to Insect Infestation",
        'DisasterMoneyLoss_DummyWS': "Money Loss due to Windstorm",
        'DisasterMoneyLoss_DummyTS': "Money Loss due to Thunderstorm",
        'DisasterMoneyLoss_DummyHS': "Money Loss due to Hailstorm",
        'DisasterMoneyLoss_DummyHR': "Money Loss due to Heavy Rain",
        'DisasterMoneyLoss_DummySR': "Money Loss due to Snowfall/Rain",
        'DisasterMoneyLoss_DummySE': "Money Loss due to Earthquake",
        'DisasterMoneyLoss_DummyLS': "Money Loss due to Landslide",
        'DisasterMoneyLoss_DummySS': "Money Loss due to Snowstorm",
        'DisasterMoneyLoss_DummyAV': "Money Loss due to Avalanche",
        'DisasterMoneyLoss_DummyGLOF': "Money Loss due to GLOF",
        'DisasterMoneyLoss_DummyHW': "Money Loss due to Heat Wave",
        'DisasterMoneyLoss_DummyCW': "Money Loss due to Cold Wave",
        'DisasterMoneyLoss_DummyDI': "Money Loss due to Disease Outbreak",
        'DisasterMoneyLoss_DummyOT': "Money Loss due to Other Disaster",
    })
    df_inuse.columns = df_inuse.columns.map(variname_readable)
    
    return df_inuse