#include<stdio.h>
int main()
{
    char buf[0x100];
    scanf("%s",buf);
    printf("%s \n",buf);
}
//Ubuntu 16.04
//gcc -fno-stack-protector ./main.c -o main
