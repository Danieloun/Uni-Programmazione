#include <stdio.h>

int main() {
    int c = 0;
    float n = 13.4;
    while (n < 0) {
        c += n%10;
        n = n/10;
    }
    printf("%d", c);
}