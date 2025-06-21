from fastapi import FastAPI
from app.predict import make_prediction
from app.schemas import PredictionInput, PredictionOutput

app = FastAPI()

@app.post("/predict", response_model=PredictionOutput)
def predict(data: PredictionInput):
    return make_prediction(data)