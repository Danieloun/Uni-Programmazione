def inverte_stringa(testo):
    if len(testo) > 0:
        invertita = testo[::-1]
        return invertita
    else:
        print("Per poter invertina una parola la devi scrivere!")


# Esempio di utilizzo:
input_stringa = ""
risultato = inverte_stringa(input_stringa)
if risultato != None:
    print(f"L'inversione di '{input_stringa}' è: '{risultato}'")
