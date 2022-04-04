#include<stdio.h>
int main()
{
    char buf[0x100];
    read(0,buf,0x200);
    write(1,buf,0x100);
}
//Ubuntu 16.04
//gcc -fno-stack-protector ./main.c -o main
