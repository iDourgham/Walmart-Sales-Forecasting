import joblib
import pandas as pd
import os
from pathlib import Path

# Load the trained model
# model_path = os.path.join("model", "xgb_model.pkl")
# model_path = os.path.join(os.getcwd(), "model", "xgb_model.pkl")
model_path = Path(__file__).resolve().parents[1] / "model" / "xgb_model.pkl"
xgb_model = joblib.load(model_path)

def predict_sales(input_df: pd.DataFrame) -> pd.Series:
    """Predict weekly sales given a DataFrame of features."""
    return xgb_model.predict(input_df)