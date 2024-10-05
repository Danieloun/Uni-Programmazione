def trovare_codici_sblocco(K):
    codici_sblocco = []
    for X in range(1, K+1):
        for Y in range(1, K+1):
            for Z in range(1, K+1):
                if X * Y + Z == K:
                    codici_sblocco.append((X, Y, Z))
    return codici_sblocco

def main():
    K = int(input("Inserisci k: "))
    codici = trovare_codici_sblocco(K)
    if codici:
        print("I possibili codici di sblocco sono: ")
        for codice in codici:
            print(codice)
    else:
        print("Non ci sono combinazioni ")

if __name__ == "__main__":
    main()
