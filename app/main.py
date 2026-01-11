from fastapi import FastAPI
from app.features import hash_feature
from app.model import predict

app = FastAPI()


@app.get("/predict")
def predict_endpoint(text: str):
    feature = hash_feature(text)
    prediction = predict(feature)
    return {"prediction": prediction}
