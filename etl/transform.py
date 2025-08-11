import os
import logging
import pandas as pd

logger = logging.getLogger("inst414.etl.transform")


def clean_steam_data(input_path: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        logger.exception(f"Raw file not found at {input_path}")
        raise

    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    if "release_date" in df.columns:
        df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
        df["release_year"] = df["release_date"].dt.year

    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

    if "tags" in df.columns and df["tags"].dtype == object:
        df["tags"] = df["tags"].apply(lambda x: [t.strip() for t in str(x).split(",")] if pd.notnull(x) else [])

    essential = [c for c in ["name", "price"] if c in df.columns]
if essential:
        df = df.dropna(subset=essential)

    df.to_csv(output_path, index=False)
    logger.info(f"Cleaned data saved to {output_path}")
