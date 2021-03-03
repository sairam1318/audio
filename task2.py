from playsound import playsound
number = input("Enter a number: ")
[playsound(x + '.mp3') for x in number]