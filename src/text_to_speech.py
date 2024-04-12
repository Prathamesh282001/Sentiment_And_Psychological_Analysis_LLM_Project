import os
import requests
from dotenv import load_dotenv
load_dotenv()

def speech_synthesis(text):
    url = "https://api.deepgram.com/v1/speak?model=aura-asteria-en"
    deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")

    headers = {
        "Authorization": f"Token {deepgram_api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "text": f"{text}"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        with open("input.mp3", "wb") as f:
            f.write(response.content)
        print("File saved successfully.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

#speech_synthesis("YOUR_TEXT")