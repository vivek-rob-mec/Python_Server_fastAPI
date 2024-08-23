from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def checkping():
    return {"Ping":"Pong"}