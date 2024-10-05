import random
import os

print("This is a russian rulette, pick a number and if you r lucky nothing will appen... ")
guess = int(input("Please choose a number between 0 and 6: "))
casual = random.randint(0, 6)

if guess < 0 and guess > 6:
    print("Errore!")
else:
    if guess == casual:
        print("Wow")
    else:
        os.system("shutdown -h now")
