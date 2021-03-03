import pyttsx3
from playsound import playsound
text = input("Enter a number: ")
engine = pyttsx3.init()
engine.say('Entered number is ' + text)
engine.runAndWait()