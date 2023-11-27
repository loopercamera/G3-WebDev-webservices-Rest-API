import uvicorn
from fastapi import FastAPI
from fastapi import responses


app = FastAPI()
app.mount

@app.get("/")
async def root():
    return{"Version" : "1.0"}

@app.get("/hallo")
async def hallo():
    return{"Hello" : "World"}


@app.get("/bild")
async def bild():
    return responses.FileResponse("static/hund.jpg")

@app.get("/web")
async def web():
    return responses.FileResponse("static/hund.jpg")



uvicorn.run(app,host="127.0.0.1" , port=8000)