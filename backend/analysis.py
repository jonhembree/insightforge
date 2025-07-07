# InsightForge – AI-Powered Business Intelligence System
# Author: Jon Hembree
# Description: Backend analysis module

import pandas as pd

def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

def run_analysis(df):
    return df.describe()
