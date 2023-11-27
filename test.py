from fastapi import FastAPI
from urllib.parse import unquote
import csv

app = FastAPI()

@app.get("/")
async def root():
    return {"Version": "1.0"}

@app.get("/{gemeinde_name_encoded}")
async def web(gemeinde_name_encoded: str):
    gemeinde_name = unquote(gemeinde_name_encoded)
    print("Decoded gemeinde_name:", gemeinde_name)

    # Open the CSV file and search for the gemeinde_name
    with open("PLZO_CSV_LV95/PLZO_CSV_LV95.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for data in reader:
            if data[0] == gemeinde_name:
                return {"data": data}  # Returning the found data

# Run the FastAPI application using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
