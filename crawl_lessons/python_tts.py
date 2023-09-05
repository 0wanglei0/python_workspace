import pyttsx3

engine = pyttsx3.init()

engine.say("hello")

with open("auto_reply.csv", "r", encoding="utf-8") as file:
    engine.say(file.read())

engine.runAndWait()