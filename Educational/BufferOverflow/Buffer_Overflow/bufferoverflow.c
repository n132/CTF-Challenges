#include<stdio.h>
void backdoor()
{
    system("/bin/sh");
    return;
}
void main(){
    char buf[0x20];
    size_t *p  = buf+0x28;
    printf("Address of backdoor: %p\n",backdoor);
    printf("Canary Value: %p\n",*(p));
    read(0,buf,0x48);
    return ;
}