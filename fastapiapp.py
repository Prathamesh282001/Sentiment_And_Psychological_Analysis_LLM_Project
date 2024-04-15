import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.speech_to_text import transcribe_audio
from src.llm import analyze_text

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Sentiment & Psychological Analysis'}


@app.post("/upload/")
def upload_file(audio: UploadFile = File(...)):
    transcribed_text = transcribe_audio(audio.filename)
    if transcribed_text:
        result = analyze_text(transcribed_text)
        return {"sentiment": result}
    else:
        return {"error": "Error occurred in upload_file function."}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)