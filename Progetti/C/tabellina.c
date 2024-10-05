#include <stdio.h>

int main() {
    int n;
    int r = n;
    printf("Inserisci un numero per sapere la sua tabellina(fino al 10): ");
    scanf("%d", &n);
    for (int i = 1; i <= 11; i++) {
        printf("%d\n", r);
        r = n * i;
        
        
    }
    
    


}