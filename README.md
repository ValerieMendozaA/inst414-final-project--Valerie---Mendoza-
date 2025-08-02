# INST414 Final Project – Valerie Mendoza

## Project Overview
This project predicts how well a video game might sell on Steam, based on public data like reviews, pricing, tags, and estimated player counts. The goal is to help game studios make smarter decisions about marketing and releases.

## Setup Instructions
1. Clone the repo:
git clone https://github.com/valeriemendoza/inst414-final-project-valerie-mendoza.git

2. Set up a virtual environment:
cd inst414-final-project-valerie-mendoza  
python -m venv venv  
source venv/bin/activate   (On Windows: venv\Scripts\activate)

3. Install the required packages:
pip install -r requirements.txt

## Running the Project
Run the full pipeline with:
python main.py

## Code Package Structure
- data/: Where your raw, cleaned, and output data files are stored.
- etl/: Scripts to extract, clean, and load data.
- analysis/: Scripts for building and evaluating models.
- vis/: Script for generating charts.
- main.py: Runs the whole project pipeline.
