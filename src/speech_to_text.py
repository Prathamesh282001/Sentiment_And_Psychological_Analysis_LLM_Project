import os
import requests
from dotenv import load_dotenv
load_dotenv()

def transcribe_audio(audio_file):
    url = "https://api.deepgram.com/v1/listen?model=enhanced"
    deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")

    
    headers = {
        "Authorization": f"Token {deepgram_api_key}",
        "Content-Type": "audio/wav"
    }
    
    files = {"content": open(audio_file, "rb")}
    
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        return response.json()["results"]["channels"][0]["alternatives"][0]["transcript"]
    else:
        return None