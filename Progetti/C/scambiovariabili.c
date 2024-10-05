#include <stdio.h>

int main() {
    printf("Prima dello scambio le variabili sono: \n");
    int a, b;
    a = 5;
    b = 10;
    printf("a = %d\nb = %d\n", a, b);

    printf("Dopo lo scambio le variabili sono: \n");
    a = a + b;
    b = a - b;
    a = a - b;
    printf("a = %d\nb = %d\n", a, b);

}