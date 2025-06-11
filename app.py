from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")

@app.route("/", methods=["GET", "POST"])
def index():
    transcription = ""
    if request.method == "POST":
        audio_file = request.files["audio"].read()
        result = transcriber(audio_file)
        transcription = result["text"]
    return render_template("index.html", transcription=transcription)

if __name__ == "__main__":
    app.run(debug=True)