import os
import pandas as pd

def clean_steam_data(input_path, output_path):

    df = pd.read_csv(input_path)

    df = df.drop_duplicates()
    # names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # missing values 
    df = df.dropna(subset=["name", "release_date", "price", "tags"], how="any")

    # Split tags 
    if "tags" in df.columns and df["tags"].dtype == object:
        df["tags"] = df["tags"].apply(lambda x: x.split(",") if isinstance(x, str) else [])

    # Save the cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    input_file = "inst414-final-project-valerie-mendoza/data/extracted/steam_games.csv"
    output_file = "inst414-final-project-valerie-mendoza/data/processed/steam_games_cleaned.csv"
    clean_steam_data(input_file, output_file)
