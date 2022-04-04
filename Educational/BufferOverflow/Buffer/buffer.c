#include<stdio.h>
char *global_buffer[0x132];
int main(){

char stack_buffer[0x132];
char *heap_buffer = malloc(0x132);

printf("The address of global_buffer:");
printf("%p\n",global_buffer);
printf("The address of stack_buffer:");
printf("%p\n",stack_buffer);
printf("The address of heap_buffer:");
printf("%p\n",heap_buffer);

}