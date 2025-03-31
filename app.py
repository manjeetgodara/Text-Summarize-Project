from fastapi import FastAPI
import uvicorn
import os
import sys
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from textSummarizer.pipeline.prediction import PredictionPipeline

text:str = "What is text Summarization?"
app = FastAPI()

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response("Training Complete")
    except Exception as e:
        return Response(f"Training Failed Error: {e}")

@app.get("/predict")
async def predict(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        return Response(f"Error: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)

