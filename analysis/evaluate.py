from sklearn.metrics import mean_squared_error, r2_score
from model import train_model

def evaluate_model():
 
    model, X_test, y_test = train_model("inst414-final-project-valerie-mendoza/data/processed/steam_games_cleaned.csv")
    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("Model Evaluation:")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R-squared (R²): {r2:.2f}")

if __name__ == "__main__":
    evaluate_model()
