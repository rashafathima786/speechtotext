import whisper
model = whisper.load_model("turbo")  
result = model.transcribe("audio1.mp3")
print(result["text"])