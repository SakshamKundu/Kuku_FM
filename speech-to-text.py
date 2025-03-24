# equired: Python 3.8 - 3.11 (using 3.10)
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
# pip install openai-whisper ffmpeg-python
# install ffmpeg from https://ffmpeg.org/download.html and add to paths


# ***** For Virtual Environment *****
# When done, deactivate it:
# deactivate

# To use it again later:
# cd C:\Users\SAKSHAM\Documents\my_project
# venv\Scripts\Activate.ps1



import whisper

# Load the base model (140MB)
model = whisper.load_model("tiny")

# Transcribe an MP3 file
result = model.transcribe("audio.mp3")

# Print the transcribed text
print(result["text"])
