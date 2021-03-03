import pyttsx3
from playsound import playsound
number = input("Enter a number: ")
engine = pyttsx3.init()
engine.say('Entered number is ' + number)
engine.runAndWait()
