print("Hello from GitHub Jenkins integration")

from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("best_model.pkl")

class InputData(BaseModel):
    features: List[float]

    

@app.get("/")
def home():
    return {"message": "ML Model API is running"}

@app.post("/predict")
def predict(input_data: InputData):
    data = np.array(input_data.features).reshape(1, -1)
    prediction = model.predict(data)
    return {"prediction": prediction.tolist()}