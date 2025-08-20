import os
import logging
import pandas as pd

logger = logging.getLogger("inst414.etl.load")

def load_cleaned_data(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        logger.error(f"Cleaned data not found: {path}")
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    logger.info(f"Loaded cleaned data with shape {df.shape}")
    return df
