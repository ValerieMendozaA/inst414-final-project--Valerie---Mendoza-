Steam Game Sales Prediction


Overview
This project predicts how well a game will sell on Steam using details like price, reviews, and tags. The pipeline pulls the data, cleans it up, loads it into the project, trains a model, and creates charts to help visualize the results.


Project Structure
data/ – folders for raw, processed, and output data

etl/ – scripts for extracting, cleaning, and loading data

analysis/ – scripts for training and evaluating the model

vis/ – scripts for making charts and graphs

main.py – runs the entire pipeline

requirements.txt – list of Python packages used


How to Run
1.Install the required packages:
pip install -r requirements.txt

2.Run the pipeline:
python main.py


Current Status
End-to-end pipeline is running
Model generates predictions
Initial charts are complete

Logging and error handling have been added

