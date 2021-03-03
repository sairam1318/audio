from playsound import playsound
number = input("Enter a number: ")
[playsound(digit + '.mp3') for digit in number]