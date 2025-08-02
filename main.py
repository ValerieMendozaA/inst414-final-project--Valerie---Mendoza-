from etl.extract import download_steam_dataset
from etl.transform import clean_steam_data
from etl.load import load_cleaned_data
from analysis.model import train_model
from analysis.evaluate import evaluate_model
from vis.visualizations import generate_visuals

def run_pipeline():
    """
   This is the full data science workflow from extraction to visualization.
    """
    # Step 1: Extract
    print("Extracting data...")
    download_steam_dataset()

    # Step 2: Transform
    print("Cleaning data...")
    input_path = "inst414-final-project-valerie-mendoza/data/extracted/steam_games.csv"
    output_path = "inst414-final-project-valerie-mendoza/data/processed/steam_games_cleaned.csv"
    clean_steam_data(input_path, output_path)

    # Step 3: Load
    print("Loading cleaned data...")
    df = load_cleaned_data(output_path)

    # Step 4: Modeling
    print("Training model...")
    model, X_test, y_test = train_model(output_path)

    # Step 5: Evaluation
    print("Evaluating model...")
    evaluate_model()

    # Step 6: Visualizations
    print("Generating visualizations...")
    generate_visuals(output_path, "inst414-final-project-valerie-mendoza/data/outputs")

    print("Pipeline complete!")

if __name__ == "__main__":
    run_pipeline()

