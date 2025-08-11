from pathlib import Path
import logging
import logging.handlers

# Local imports
from etl.extract import download_steam_dataset
from etl.transform import clean_steam_data
from etl.load import load_cleaned_data
from analysis.model import train_model
from analysis.evaluate import evaluate_and_save_metrics
from vis.visualizations import generate_visuals



BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
EXTRACTED = DATA_DIR / "extracted" / "steam_games.csv"
PROCESSED = DATA_DIR / "processed" / "steam_games_cleaned.csv"
OUTPUTS = DATA_DIR / "outputs"
LOGS_DIR = BASE_DIR / "logs"
LOG_FILE = LOGS_DIR / "app.log"


def setup_logger():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("inst414")
    logger.setLevel(logging.INFO)


    fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=2)
    fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)

  
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger


def run_pipeline():
    logger = setup_logger()
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "extracted").mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "processed").mkdir(parents=True, exist_ok=True)

    logger.info("=== START PIPELINE ===")

 
    try:
        logger.info("Step 1: Extracting data…")
        download_steam_dataset(str(EXTRACTED))
        logger.info(f"Raw data saved to {EXTRACTED}")
    except Exception as e:
        logger.exception("Extract step failed but continuing.")
    
   
    try:
        logger.info("Step 2: Cleaning data…")
        clean_steam_data(str(EXTRACTED), str(PROCESSED))
        logger.info(f"Cleaned data saved to {PROCESSED}")
    except Exception as e:
        logger.exception("Transform step failed but continuing.")
    
   
    df = None
    try:
        logger.info("Step 3: Loading cleaned data…")
        df = load_cleaned_data(str(PROCESSED))
        logger.info(f"Loaded cleaned dataframe with shape {getattr(df, 'shape', None)}")
    except Exception as e:
        logger.exception("Load step failed but continuing.")

   
    model = None
    try:
        logger.info("Step 4: Training model…")
        model, X_test, y_test = train_model(str(PROCESSED), outputs_dir=str(OUTPUTS))
        logger.info("Model trained.")
    except Exception as e:
        logger.exception("Model training failed but continuing.")

    
    try:
        logger.info("Step 5: Evaluating model…")
        evaluate_and_save_metrics(str(PROCESSED), outputs_dir=str(OUTPUTS))
        logger.info("Saved metrics to outputs.")
    except Exception as e:
        logger.exception("Evaluation failed but continuing.")

    try:
        logger.info("Step 6: Generating visuals…")
        generate_visuals(str(PROCESSED), str(OUTPUTS))
        logger.info("Visuals written to outputs.")
    except Exception as e:
        logger.exception("Visualization step failed but continuing.")

    logger.info("=== END PIPELINE ===")


if __name__ == "__main__":
    run_pipeline()
