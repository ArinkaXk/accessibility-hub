from transformers import pipeline

# Initialize Whisper
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-tiny")

# Transcribe sample audio
audio_file = "test2.mp4"  # Replace with a sample
result = transcriber(audio_file)
print("Transcription:", result["text"])
with open("output.txt", "w") as f:
    f.write(result["text"])