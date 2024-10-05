import random

print("Giochiamo a sasso carta forbice! Che vinca il migliore.\n ")
print("Il computer ha scelto la sua mossa! ")

scelta = input("Scrivi cosa vuoi buttare:\n (Indica solo l iniziale ex: s, c, f)\n")
possibilita = ["s", "c", "f"]
computer = random.choice(possibilita)
nome = ""

if computer == "s":
    nome += "sasso"
elif computer == "f":
    nome += "forbice"
elif computer == "c":
    nome += "carta"

print("Il computer ha scelto... ", nome)
# s>f, f>c, c>r

if scelta == computer:
    print("PAREGGIO!")
elif scelta == "s" and computer == "f" or scelta == "f" and computer == "c" \
or scelta == "c" and computer == "r":
    print("HAI VINTO!")
else:
    print("HAI PERSO!")


