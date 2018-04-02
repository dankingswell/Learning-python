import requests
import pyttsx

engine = pyttsx.init()
engine.say(engine.say(requests.get("https://icanhazdadjoke.com/", headers = {
    "Accept" : "text/plain"
}).text))
engine.runAndWait()


