import pyttsx3

engine = pyttsx3.int('sapi5')# for voise used sapi5
voices = engine.getProperty('voices')
print(voices[1].id)

engine.setProperty('voice',voices[0].id)

def speak(audio):