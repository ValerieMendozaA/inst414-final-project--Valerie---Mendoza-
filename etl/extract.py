import os
import pandas as pd
import requests

def download_steam_dataset():
    url = "https://huggingface.co/datasets/FronkonGames/steam-games-dataset/resolve/main/steam_games.csv"
    output_dir = "inst414-final-project-valerie-mendoza/data/extracted"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "steam_games.csv")

    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print("Dataset downloaded and saved to:", output_path)
    else:
        print("Failed to download dataset. Status code:", response.status_code)

if __name__ == "__main__":
    download_steam_dataset()
