#include <stdio.h>
#include <stdlib.h>
void n132(){
    char buf[0x30]={0};
    int f = open("./flag",0);
    read(f,buf,0x30);
    write(1,buf,0x30);
}
void vul(){
    char buf[100];
    read(0,buf,0x4000);
}
void pthread_f(){
    vul();
}
int main(){
    pthread_t pid; 
    pthread_create(&pid,0,pthread_f,0);
    while(1);
    return 0;
}
/*
000000123123

tcb
...
000000
...


*/