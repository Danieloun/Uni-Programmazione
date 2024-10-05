#include <stdio.h>
#include <math.h>

int main() {
    printf("Questo programmma calcola la potenza di un numero.\n");
    double a = 0;
    double n = 0;
    printf("Inserisci la base: ");
    scanf("%lf", &a);
    printf("Inserisci l'esponente: ");
    scanf("%lf", &n);
    int risultato = pow(a, n);
    printf("Il risultato è %d", risultato);

}