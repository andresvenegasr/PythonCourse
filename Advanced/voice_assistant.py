import re

import pyttsx3
import speech_recognition as sr

# install pipwin to install pyaudio -- pipwin install pyaudio

engine = pyttsx3.init()
engine.setProperty("rate", 120)
engine.setProperty("voice", "spanish")

engine.say("Hola, ¿Cómo estás?")
engine.runAndWait()

# pip install SpeechRecognition

r = sr.Recognizer()

with sr.Microphone as source:
    print("Puedes hablar")
    audio = r.listen(source)
    text = r.recognize_google(audio, language="es-MX")
    name = re.findall("me llamo ([A-Za-z]+)", text)
    engine.say("Encantado de conocerte, {}".format(name[0]))
    engine.runAndWait()