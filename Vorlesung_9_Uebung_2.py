import uvicorn
from fastapi import FastAPI, Query
from fastapi import responses
from urllib.parse import unquote

import pyproj
from pyproj import Transformer

import csv

lv95 = "EPSG:2056"
wgs84 = "EPSG:4326"

app = FastAPI()
app.mount

@app.get("/")
async def root():
    return{"Version" : "1.0"}


@app.get("/wgs84lv95")
async def wgs84lv95(lng: float = Query(...),lat: float = Query(...) ):
    t1 = Transformer.from_crs(wgs84,lv95)
    data = t1.transform(lat,lng)
    return {"E" : data[0],    "N" : data[1] }
#&lat={lat}"

uvicorn.run(app,host="127.0.0.1" , port=8000)