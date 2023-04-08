#include<stdio.h>
#include<string.h>
int main(){
    char buf[0x100];
    while(1){
        memset(buf,0,0x100);
        size_t res = read(0,buf,0x100);
        if(res==0x100)
            break;
        printf(buf);
        printf("\n");
    }   
}