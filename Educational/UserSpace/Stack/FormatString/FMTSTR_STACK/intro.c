#include<stdio.h>
#include<string.h>
int main(){
    char buf[0x100];
    while(1){
        memset(buf,0,0x100);
        read(0,buf,0x100);
        if(!strcmp(buf,"exit"))
            break;
        printf(buf);
        printf("\n");
    }   
}