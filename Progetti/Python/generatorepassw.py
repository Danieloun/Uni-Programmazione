import random

print("This program will gen a random password for you.")

n = int(input("How many password do you need? "))
l = int(input("How long do you want your password be? "))
lib = "zxcvbnmlkjhgfdsaqwertyuiopè+ùàò,.-ZXCVBNMLKJHGFDSAQWERTYUIOP;:_ç°§é*1234567890"

for x in range(n):
    password = ""
    for y in range(l):
        password += random.choice(lib)

    print(password)
