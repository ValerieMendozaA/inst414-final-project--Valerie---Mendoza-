# Steam Game Sales Prediction Pipeline 🎮

Hi! This project is about predicting how well a video game will sell on Steam using a full data science pipeline. It goes from raw data to clean visuals, and everything is handled through code just run one file and it walks through the whole process.

---

## What the Code Does

When you run `main.py`, here’s what happens:

1. Uses the Steam dataset you provide  
2. Cleans and processes the data  
3. Trains a linear regression model  
4. Evaluates the model using MSE and R²  
5. Creates visualizations that show insights into game performance

---

## Project Structure

- `etl/` – handles extraction, transformation, and loading of the data  
- `analysis/` – runs modeling and evaluation  
- `vis/` – generates all charts and visuals  
- `data/` – contains reference tables and output folders  
- `logs/` – stores logs for each pipeline run  
- `main.py` – this is the file that runs everything

---

## How to Run It

1. **Install the required Python packages**  
Open your terminal and run:
```bash
pip install -r requirements.txt

Download the dataset manually
The dataset is too large to include in GitHub; I had to download it myself:

Link: https://huggingface.co/datasets/FronkonGames/steam-games-dataset/blob/main/games.csv

After downloading, rename the file to:

steam_games.csv


Then place it inside this folder:

data/extracted/


Run the pipeline
Once the dataset is in the right place, just run:

python main.py


It’ll go through the whole pipeline — from cleaning the data to training the model and generating visualizations. You’ll find the outputs in the data/outputs/ folder.
