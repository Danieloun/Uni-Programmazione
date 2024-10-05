#include <stdio.h>
#include <string.h>

int contavocali(const char *frase){
    int contatore = 0;
    int lunghezza = strlen(frase);
    
    for (int i = 0; i < lunghezza; i++) {
        char carattere = tolower(frase[i]);

        if (carattere == "a" || carattere == "e" || carattere == "i" || carattere == "o" || carattere == "u") {
            contatore++;
        }
        
    }
    return contatore;

}

int main() {
    char frase[100];
    printf("Inserisci una stringa: ");
    fgets(stringa, sizeof(stringa), stdin);

}