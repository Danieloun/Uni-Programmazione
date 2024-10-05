#include <stdio.h>
#include <math.h>

int main() {
    printf("This program will calculate your compound interess.\n");
    //define the variables
    double amount, time, rate;
    printf("Type the amount: ");
    scanf("%lf", &amount);      
    printf("Type for how long (year) you want to calculate the interest: ");
    scanf("%lf", &time);
    printf("Type the rate of your interest (float): ");
    scanf("%lf", &rate);

    //calculate the interest i = a(1 + r)^t 

    double interest = amount*(pow((1 + rate/100), time));
    double CI = interest - amount;

    printf("%lf", CI);


}