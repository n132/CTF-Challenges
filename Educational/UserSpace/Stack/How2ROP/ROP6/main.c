#include<stdio.h>
int main()
{
    char buf[0x10];
    gets(buf);
    return 0x132;
    //Zexin Li, don't choose this challenge, or you would wast tons of hours.
}
//Ubuntu 16.04
//gcc -fno-stack-protector ./main.c -o main
