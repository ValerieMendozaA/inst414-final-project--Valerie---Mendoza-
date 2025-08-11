# Steam Game Sales Prediction
## What this project is about
I’m building a pipeline to guess how well a game will sell on Steam using data like price, reviews, and tags. The pipeline gets the data, cleans it, loads it, trains a model, and makes some charts.

## What’s in the project
data/ – where the raw, cleaned, and output files go

etl/ – scripts to get, clean, and save the data

analysis/ – scripts to train and check the model

vis/ – makes the charts and graphs

main.py – runs the whole thing

requirements.txt – list of packages you need

## How to run it
Install the packages:
pip install -r requirements.txt

Run the pipeline:
python main.py

## Right now
Pipeline works from start to finish

Model gives predictions

Some charts are ready

Logging and error handling are in place

