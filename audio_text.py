import io
import os
import requests
import json
from google.cloud import speech_v1p1beta1 as speech

# Set the Google Cloud credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/credentials.json"

# Define the Speech-to-Text API client
client = speech.SpeechClient()

# Define the audio file path
audio_file_path = "path/to/audio/file.wav"

# Read the audio file content
with io.open(audio_file_path, "rb") as audio_file:
    content = audio_file.read()

# Define the Speech-to-Text API configuration
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
    enable_speaker_diarization=True,
    diarization_speaker_count=2,
)

# Define the audio input
audio = speech.RecognitionAudio(content=content)

# Transcribe the audio
response = client.recognize(config=config, audio=audio)

# Get the transcription results
results = response.results

# Loop through the transcription results
for result in results:
    # Get the transcription text
    transcript = result.alternatives[0].transcript
    # Get the speaker tag
    speaker_tag = result.alternatives[0].speaker_tag
    # Print the transcription text and speaker tag
    print(f"Speaker {speaker_tag}: {transcript}")
