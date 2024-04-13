"""import os
from flask import Flask, request, render_template
from src.speech_to_text import transcribe_audio
from src.llm import analyze_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return "No audio file uploaded"

    audio_file = request.files['audio']

    if audio_file.filename == '':
        return "No selected file"

    temp_file_path = "/tmp/" + audio_file.filename
    audio_file.save(temp_file_path)

    transcribed_text = transcribe_audio(temp_file_path)

    if transcribed_text:
        result = analyze_text(transcribed_text)
        return render_template('index.html', output=result)
    else:
        return "Error in transcription"

if __name__ == '__main__':
    app.run(debug=True)
"""
from flask import Flask, request, render_template
from src.speech_to_text import transcribe_audio
from src.llm import analyze_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    audio_file = request.files['audio']
    
    transcribed_text = transcribe_audio(audio_file.filename)
    if transcribed_text:
        result = analyze_text(transcribed_text)
        return render_template('index.html', output=result)
    else:
        return "Error in upload function."

if __name__ == '__main__':
    app.run(debug=True)