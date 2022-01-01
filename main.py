from art import logo
from art import caeser
print(logo)
Final = True
while Final:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caeser(text, shift, direction)
    restart = input('Type yes if you want to go again Otherwise type no :\n')
    if restart == "no":
        Final = False
        print("Good Bye")

