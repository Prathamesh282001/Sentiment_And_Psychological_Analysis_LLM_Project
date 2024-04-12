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