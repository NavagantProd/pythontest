from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/message")
def get_message():
    return JSONResponse(content={"message": "Hello from Python microservice!"})
