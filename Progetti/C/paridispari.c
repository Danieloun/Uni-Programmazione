#include <stdio.h>

int main() {
    int n; 
    printf("Digita un numero verificherò se è paro o disparo: ");
    scanf("%d", &n);
    if (n % 2 == 0) {
        printf("Il numero è pari.");
    }
    else {
        printf("Il numero è dispari.");
    }
}