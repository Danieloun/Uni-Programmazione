def calcola_mediana(lista):
    ordinata = sorted(lista)
    n = len(ordinata)
    if n % 2 == 0:   #caso pari
        a = ordinata[(n-1)//2]
        b = ordinata[(n)//2]
        risultato = (a + b)/2
    else: #caso dispari        
        risultato = ordinata[n//2]
    return risultato
    


# Esempio di utilizzo:
numeri = [4, 2, 8, 5, 1, 7, 6]
risultato = calcola_mediana(numeri)
print("Mediana:", risultato)