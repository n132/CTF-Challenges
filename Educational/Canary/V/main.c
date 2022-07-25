#include <stdio.h>
#include <stdlib.h>
void n132(){
    system("/bin/sh");
}
int main(){
    size_t addr;
    printf("%p\n",main);
    read(0,&addr,8);
    read(0,addr,8);
    char buf[0x100];
    read(0,buf,0x109);
}