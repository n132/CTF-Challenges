#include<stdio.h>
#include<stdint.h>
int main()
{
    size_t p[0x30];
    size_t ct = 0 ; 

    p[ct++] = malloc(0x500);//0
    p[ct++] = malloc(0x88);//1
    p[ct++] = malloc(0x88);//2
    free(p[0]);
    p[ct++] = malloc(0x18);//3
    *((uint8_t *)p[3]+0x18)= 0 ; 
    p[ct++] = malloc(0x88);//4
    p[ct++] = malloc(0x88);//5
    free(p[4]);
    free(p[1]);

}