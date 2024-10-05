def verifica_palindromo(stringa):
    stringa = stringa.lower()
    stringa = stringa.replace(" ", "")
    return stringa == stringa[::-1]





# Esempio di utilizzo:
parola = "radar"
risultato = verifica_palindromo(parola)
print(f"'{parola}' è un palindromo? {risultato}")
