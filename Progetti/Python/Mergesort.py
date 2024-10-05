# siano a e b due liste ordinate
# scrivere una funzione che ordini gli elementi 
# di a e b in una nuova lista

a = [1, 3, 5, 7, 9, 11, 13, 15]
b = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

def merge(a, b):
    a.extend(b)

    n = len(a)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1] , a[j]

    return a

print("The default lists are ", a," e ", b)

print("The ordered list is ", merge(a, b))


