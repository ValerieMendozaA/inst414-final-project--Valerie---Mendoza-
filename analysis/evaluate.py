import os
import logging
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from analysis.model import train_model

logger = logging.getLogger("inst414.analysis.evaluate")


def evaluate_and_save_metrics(processed_csv: str, outputs_dir: str = "data/outputs"):
    os.makedirs(outputs_dir, exist_ok=True)
    model, X_test, y_test = train_model(processed_csv, outputs_dir)
    y_pred = model.predict(X_test)

    mse = float(mean_squared_error(y_test, y_pred))
    r2 = float(r2_score(y_test, y_pred))

    pd.DataFrame(
        [{"metric": "MSE", "value": mse}, {"metric": "R2", "value": r2}]
    ).to_csv(os.path.join(outputs_dir, "metrics.csv"), index=False)

    with open(os.path.join(outputs_dir, "metrics.txt"), "w") as f:
        f.write(f"MSE: {mse:.4f}\nR2: {r2:.4f}\n")

    logger.info("Saved metrics to data/outputs.")
