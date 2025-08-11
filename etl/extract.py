import os
import logging
import requests

logger = logging.getLogger("inst414.etl.extract")


def download_steam_dataset(output_path: str):
   
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    url = "https://huggingface.co/datasets/FronkonGames/steam-games-dataset/resolve/main/steam_games.csv"
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(r.content)
        logger.info(f"Downloaded dataset to {output_path}")
    except Exception:
        logger.exception("Failed to download dataset.")
        raise
