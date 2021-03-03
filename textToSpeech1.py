import pyttsx3
from playsound import playsound
text = input("Enter a text: ")
engine = pyttsx3.init()
engine.say('Entered text is {}'.format(text))
engine.runAndWait()