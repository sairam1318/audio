from playsound import playsound
givenNumber = input("Enter a number: ")
[playsound(x + '.mp3') for number in givenNumber]
