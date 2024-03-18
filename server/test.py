import whisper as wh

model = wh.load_model("medium")

result = model.transcribe("audio\\file_buono.wav", language="it", fp16=False)
print(result["text"])
result = model.transcribe("audio\\file.wav", language="it", fp16=False)
print(result["text"])

