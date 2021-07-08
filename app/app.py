from fastapi import FastAPI, Body
import pickle
from pydantic import BaseModel, conlist
from typing import List


app = FastAPI(title="Iris ML API", description="API for iris dataset ml model", version="1.0")


# 入力の型定義
class IrisItem(BaseModel):
    data: List[conlist(float, min_items=4, max_items=4)]  # conlist: constrained list

# 出力の型定義
class IrisPrediction(BaseModel):
    prediction: List[int]
    prediction_proba: List[conlist(float, min_items=3, max_items=3)]


# 起動後に実行
@app.on_event('startup')
async def load_model():
    global model
    with open('iris_v1.pkl', 'rb') as f:
        model = pickle.load(f)

@app.post('/predict', response_model=IrisPrediction)
async def predict_species(data_json: IrisItem):
    data = dict(data_json)['data']
    prediction = model.predict(data).tolist()
    prediction_proba = model.predict_proba(data).tolist()
    return {"prediction": prediction,
            "prediction_proba": prediction_proba}