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

1. Install the required packages:
```bash
pip install -r requirements.txt
Download the dataset manually.
Go to this link:
https://huggingface.co/datasets/FronkonGames/steam-games-dataset/blob/main/games.csv
Click the download button, save the file, and rename it to:

Copy
Edit
steam_games.csv
Then place the file into this folder in your project:

bash
Copy
Edit
data/extracted/



Run the pipeline by entering:

bash
Copy
Edit
python main.py
