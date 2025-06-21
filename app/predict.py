import pickle
import numpy as np
from pathlib import Path
from app.schemas import PredictionInput, PredictionOutput

MODEL_PATH = Path(__file__).parent / "model" / "random_forest_pipeline.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def make_prediction(data: PredictionInput) -> PredictionOutput:
    input_data = np.array([data.features])  # must match training shape
    prediction = model.predict(input_data)[0]
    return PredictionOutput(prediction=prediction)