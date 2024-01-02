# Dependencies
from fastapi import FastAPI
from Fighters import fighters_data, fighters_weightclass
from typing import List, Dict
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = FastAPI()

#get all weight classes
ufc_fights = pd.read_csv('csv_data/ufc_fight_data.csv')
weight_classes = ufc_fights.weight_class.unique().tolist()
weight_classes = weight_classes[:-1]

#route to get weightclass list
@app.get('/weight-classes')
async def get_weight_classes():
    return {"weight_classes": weight_classes}

#route to get weightclass list
@app.get('/fighters/{weight}')
async def get_fighters_by_weightclass(weight: str):
    return {"fighters": fighters_weightclass(weight)}
