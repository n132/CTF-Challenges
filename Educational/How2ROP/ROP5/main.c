#include<stdio.h>
int n132()
{
    char buf[0x100];
    buf[read(0,buf,0x100)]=0;
    puts(buf);
}
int main()
{
	char buf[0x10];
	buf[0]=1;
	n132();
}
//gcc -fno-stack-protector ./main.c -o main
