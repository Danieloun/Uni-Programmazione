#include <stdio.h>

int main(){
    
    printf("Simple calcultor.\n");
    printf("You can only type 2 numbers.\n");
    //variabili
    char segno;
    double x, y;
    printf("Enter the two numbers");
    scanf("%lf %lf", &x, &y);

    printf("Enter the operator (choose between: + - * / ): \n");
    scanf("%c", &segno);

    switch (segno){
    case '+':
        printf("%lf", x+y);
        break;
    case '-':
        printf("%lf", x-y);
        break;
    case '*':
        printf("%lf", x*y);
        break;
    case '/':
        printf("%lf", x/y);
        break;
    default:
        printf("Please enter a valid operator.\n");
    }




}