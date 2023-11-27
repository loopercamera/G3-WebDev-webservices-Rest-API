import uvicorn
from fastapi import FastAPI
from fastapi import responses
from urllib.parse import unquote

import csv


app = FastAPI()
app.mount

@app.get("/")
async def root():
    return{"Version" : "1.0"}


@app.get("/{gemeinde_name_encoded}")
async def web(gemeinde_name_encoded: str):
    print(gemeinde_name_encoded)
    gemeinde_name = unquote(gemeinde_name_encoded)
    print(gemeinde_name)
    file = open("PLZO_CSV_LV95/PLZO_CSV_LV95.csv", "r", encoding="utf-8")
    reader = csv.reader(file, delimiter=";")
    for data in reader:
        if data[0] == gemeinde_name:
            return(data)

uvicorn.run(app,host="127.0.0.1" , port=8000)