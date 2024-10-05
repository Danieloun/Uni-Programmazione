def conta_occorrenze(frase, parola):
    fra = frase.lower()
    par = parola.lower()

    occorrenze = fra.count(par)
    return occorrenze

# Esempio di utilizzo:
frase = "Questo è un esercizio di conteggio occorrenze. L'esercizio è interessante."
parola_da_contare = "esercizio"
risultato = conta_occorrenze(frase, parola_da_contare)
print(f"La parola '{parola_da_contare}' compare nella frase {risultato} volte.")
