def conta_int(arr):
    conta = 0
    somma = 0
    n = len(arr)
    for i in range(n):
        if isinstance(arr[i], int):
            conta += 1
            somma += arr[i]
    print(somma, conta)


lista = ["daniele", 22, 30, 12, "Marc", "Eso", "Ulrich", 14, 17]
print("The gave list is this: ", lista)
conta_int(lista)

