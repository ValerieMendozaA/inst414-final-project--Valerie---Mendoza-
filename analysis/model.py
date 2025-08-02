import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os
def train_model(data_path):
    df = pd.read_csv(data_path)
    features = ["price", "positive_ratings", "negative_ratings"]
    target = "owners"

    # missing data
    df = df.dropna(subset=features + [target])
    X = df[features]
    y = df[target]

  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    print("Model trained.")
    return model, X_test, y_test
if __name__ == "__main__":
    data_file = "inst414-final-project-valerie-mendoza/data/processed/steam_games_cleaned.csv"
    model, X_test, y_test = train_model(data_file)
