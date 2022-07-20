#include<stdio.h>
#include <stdlib.h>
void n132(){
    system("/bin/sh");
}
void vul(){
    char buf[100];
    read(0,buf,0x100);
    return;
}
int main(){
    while(1){
        int pid = fork();
        if(pid){
            wait(0);
        }else{
            vul();
            puts("n132");
            exit(1);
        }
    }
}