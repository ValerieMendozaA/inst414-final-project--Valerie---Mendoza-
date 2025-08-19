# Steam Game Sales Prediction Pipeline

This project predicts video game sales based on Steam data using a full data pipeline.

---

## What the Code Does

When you run `main.py`, it will:

1. Download or use the Steam dataset  
2. Clean and process the data  
3. Train a linear regression model  
4. Evaluate the model with MSE and R²  
5. Create visualizations

---

## Project Folders

- `etl/` – code for downloading, cleaning, and loading data  
- `analysis/` – model training and evaluation  
- `vis/` – charts and plots  
- `data/` – data files (only the dictionary is included)  
- `logs/` – where pipeline logs go  
- `main.py` – runs the full pipeline

---

## How to Run

1. First, install all the necessary Python packages by running:
```bash
pip install -r requirements.txt
Next, the dataset needs to be downloaded manually.
It’s not included in the repository due to size restrictions.
Please use this link to download the file:
https://huggingface.co/datasets/FronkonGames/steam-games-dataset/blob/main/games.csv

After downloading it, rename the file to:

Copy
Edit
steam_games.csv
Then place the file into this folder inside the project:

bash
Copy
Edit
data/extracted/
Once the dataset is in place, run the pipeline by using:

bash
Copy
Edit
python main.py
