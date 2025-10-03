from fastapi import FastAPI,Cookie,Path,Query,Header
from pydantic import BaseModel,Field,EmailStr #IMPORTINHG ESSSENTIAL LIBARIOES
from typing import Annotated
import joblib

model = joblib.load("cancer_model.pkl") #LOADING THE MODEL
app=FastAPI()
#DEFINING PYDANTIC MODEL FOR FEATURES
class Features(BaseModel):
    #mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness
    mean_texture:float
    mean_perimeter:float
    mean_area:float
    mean_smoothness:float

@app.get("/home")
async def mains():
    return {"Message":"BREAST CANCER PREDICTIONS ML MODEL IS DEPLOYED"}
@app.post("/predict") #PREDICTING RESULTS
async def predictions(f1:Features):
     data = [[
        f1.mean_texture,
        f1.mean_perimeter,
        f1.mean_area,
        f1.mean_smoothness
    ]]
     prediction = model.predict(data)[0]
     return {"prediction": int(prediction)}