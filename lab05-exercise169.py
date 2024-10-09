'''
Author: Jack Temko
KUID: 3161174
Date: 10/02/2024
Lab: lab05
Last modified: 10/02/2024
Purpose: Wheel! Of! Python!
'''

target = "better luck tomorrow"

print("Let's play WHEEL OF PYTHON")

hint = ""
while True:
    hint = input("Choose 5 letters to help: ").lower()
    if len(hint) == 5:
        break

out = ""
for letter in target:
    if letter == " ":
        out += " "
    elif letter.lower() in hint:
        out += letter.upper()
    else:
        out += "?"

print(out)

guess = input("Enter your guess: ").lower()
if guess == target:
    print("You win!")
else:
    print("You loose!")