import time

print("This is a TIMER.")

tempo = int(input("Choose the timer lenght: "))

while tempo > 0:
    tempo = tempo - 1
    print(tempo)
    time.sleep(1)


 
