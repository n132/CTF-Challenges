#include <stdio.h>
#include <stdlib.h>
int main(){
    printf("%p\n",printf);
    size_t addr = 0;
    read(0,&addr,sizeof(size_t));
    read(0,addr,sizeof(size_t));
    char buf[100];
    read(0,buf,0x100);
    return;
}