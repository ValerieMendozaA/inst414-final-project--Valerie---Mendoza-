# inst414-final-project--Valerie---Mendoza-
# INST414 Final Project – Valerie Mendoza

## What This Project Is About
This project focuses on predicting how well a video game might sell on Steam. The idea is to help game studios plan better, like budgeting for marketing or figuring out when to release updates. I used public data that includes game details such as price, tags, reviews, and player numbers.

## What I Used
- Steam Games dataset from Hugging Face: https://huggingface.co/datasets/FronkonGames/steam-games-dataset
- Steam player data from Mendeley: https://data.mendeley.com/datasets/ycy3sy3vj2/1

## What I Did
- Pulled and cleaned up the data (ETL)
- Built a prediction model using linear regression
- Measured how well the model worked
- Created some charts to show the data

## How To Set It Up

1. Clone the repo:
git clone https://github.com/valeriemendoza/inst414-final-project-valerie-mendoza.git

2. Start a virtual environment:
cd inst414-final-project-valerie-mendoza
python -m venv venv
source venv/bin/activate  # or use venv\Scripts\activate if you're on Windows


3. Install the required libraries:
pip install -r requirements.txt


## How To Run It
Run the main pipeline script:
python main.py


## What's In The Project Folder
```
inst414-final-project-valerie-mendoza/
├── data/                  # Holds all the data files
│   ├── extracted/         # Raw files pulled from online
│   ├── processed/         # Cleaned-up files
│   ├── outputs/           # Charts and other results
│   └── reference-tables/  # Static files like data dictionary
├── etl/                   # Scripts to extract, clean, and load data
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── analysis/              # Scripts to train and evaluate models
│   ├── model.py
│   └── evaluate.py
├── vis/                   # Code to generate visualizations
│   └── visualizations.py
├── main.py                # Runs the full project workflow
├── README.md              # This file
└── requirements.txt       # Python package list
