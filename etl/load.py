"""
loading step of the ETL pipeline
"""

import pandas as pd
import os

def load_cleaned_data(path):
    
    if os.path.exists(path):
        df = pd.read_csv(path)
        print("Cleaned data loaded successfully. Shape:", df.shape)
        return df
    else:
        raise FileNotFoundError(f"File not found at {path}")

if __name__ == "__main__":
    cleaned_file_path = "inst414-final-project-valerie-mendoza/data/processed/steam_games_cleaned.csv"
    df = load_cleaned_data(cleaned_file_path)

    
    print(df.head())
