#include<stdio.h>
void n132(){
    system("/bin/sh");
}
int main(){
    int off = 0 ; 
    void* buf[12];
    scanf("%d",&off);
    printf("%p\n",buf[off]);
    read(0,buf,0x100);
    return;
}