from playsound import playsound
givenNumber = input("Enter a number: ")
[playsound(digit + '.mp3') for digit in givenNumber]
