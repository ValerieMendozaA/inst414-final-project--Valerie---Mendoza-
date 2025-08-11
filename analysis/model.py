import os
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from joblib import dump

logger = logging.getLogger("inst414.analysis.model")

def _safe_columns(df, wanted):
    return [c for c in wanted if c in df.columns]

def train_model(processed_csv: str, outputs_dir: str = "data/outputs"):
    os.makedirs(outputs_dir, exist_ok=True)
    df = pd.read_csv(processed_csv)

  
    target_candidates = [c for c in ["owners", "owner_estimate"] if c in df.columns]
    if not target_candidates:
        df["owner_estimate"] = 0  
        target = "owner_estimate"
        logger.warning("No owners/owner_estimate in data; using dummy target.")
    else:
        target = target_candidates[0]

 
    features = _safe_columns(df, ["price", "positive_ratings", "negative_ratings", "release_year"])
    if not features:
        features = [c for c in df.select_dtypes(include="number").columns if c != target]

    df = df.dropna(subset=features + [target])
    if df.empty:
        logger.warning("No rows left after NA drop; using tiny dummy frame.")
        df = pd.DataFrame({target: [0, 1], "price": [0.0, 1.0]})
        features = ["price"]

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    dump(model, os.path.join(outputs_dir, "baseline_model.joblib"))
    logger.info("Model trained and saved.")
    return model, X_test, y_test
