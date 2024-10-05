def somma_cifre(numero):
    numero_str = str(numero)
    somma = 0

    for i in numero_str:
        i = int(i)
        somma += i
    return somma



# Esempio di utilizzo:
numero = 12345
risultato = somma_cifre(numero)
print(f"La somma delle cifre di {numero} è: {risultato}")
