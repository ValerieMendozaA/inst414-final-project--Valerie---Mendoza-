from pathlib import Path
import logging
import logging.handlers

from etl.extract import download_steam_dataset
from etl.transform import clean_steam_data
from etl.load import load_cleaned_data
from analysis.model import train_model
from analysis.evaluate import evaluate_and_save_metrics
from vis.visualizations import generate_visuals

# Paths
BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
EXTRACTED = DATA / "extracted" / "steam_games.csv"
PROCESSED = DATA / "processed" / "steam_games_cleaned.csv"
OUTPUTS = DATA / "outputs"
LOGS = BASE / "logs"
LOG_FILE = LOGS / "app.log"


def setup_logger():
    LOGS.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("inst414")
    logger.setLevel(logging.INFO)

    fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=2)
    ch = logging.StreamHandler()

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)

    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger


def run_pipeline():
    logger = setup_logger()
    (DATA / "extracted").mkdir(parents=True, exist_ok=True)
    (DATA / "processed").mkdir(parents=True, exist_ok=True)
    OUTPUTS.mkdir(parents=True, exist_ok=True)

    logger.info("=== START PIPELINE ===")

    # 1) Extract
    try:
        logger.info("Extracting data…")
        download_steam_dataset(str(EXTRACTED))
    except Exception:
        logger.exception("Extract failed (continuing).")

    # 2) Transform
    try:
        logger.info("Transforming data…")
        clean_steam_data(str(EXTRACTED), str(PROCESSED))
    except Exception:
        logger.exception("Transform failed (continuing).")

    # 3) Load
    df = None
    try:
        logger.info("Loading cleaned data…")
        df = load_cleaned_data(str(PROCESSED))
        logger.info(f"Loaded cleaned data shape: {getattr(df, 'shape', None)}")
    except Exception:
        logger.exception("Load failed (continuing).")

    # 4) Train
    try:
        logger.info("Training model…")
        train_model(str(PROCESSED), outputs_dir=str(OUTPUTS))
    except Exception:
        logger.exception("Model training failed (continuing).")


    try:
        logger.info("Evaluating model…")
        evaluate_and_save_metrics(str(PROCESSED), outputs_dir=str(OUTPUTS))
    except Exception:
        logger.exception("Evaluation failed (continuing).")

    # 6) Visualize
    try:
        logger.info("Generating visuals…")
        generate_visuals(str(PROCESSED), str(OUTPUTS))
    except Exception:
        logger.exception("Visualization failed (continuing).")

    logger.info(" END PIPELINE ")


if __name__ == "__main__":
    run_pipeline()
