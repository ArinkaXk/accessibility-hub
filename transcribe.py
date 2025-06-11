import os
from transformers import pipeline

# Check if audio file exists
audio_file = "test2.wav"  # Replace with your audio file
if not os.path.exists(audio_file):
    print(f"Error: {audio_file} not found. Please place a WAV file in the project folder.")
    exit(1)

# Initialize Whisper on CPU
try:
    transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-tiny", device=-1)
    print("Whisper model loaded successfully")
except Exception as e:
    print(f"Error loading Whisper: {e}")
    exit(1)

# Transcribe audio
try:
    result = transcriber(audio_file)
    transcription = result.get("text", "Transcription failed")
    print("Transcription:", transcription)
    
    # Save to file
    with open("output.txt", "w") as f:
        f.write(transcription)
    print("Transcription saved to output.txt")
except Exception as e:
    print(f"Error during transcription: {e}")