#include <stdio.h>
#include <stdlib.h>
size_t FLAG=0;
char *array[0x10]={0};
void menu(){
	puts("1.Add a note");
	puts("2.Delete a note");
	// puts("3.Edit a note");
	// puts("4.Exit");
	printf(">");
}
int  readint(){
	char buf[0x10];
	read(0,buf,0x10);
	return atoi(buf);
}
void add(){
	int i=0;
	for(i=0;i<0x10;i++){
		if(array[i]==0)
			break;
	}
	char *tmp=malloc(0);
	if(tmp > 0){
		array[i]=tmp;
		read(0,array[i],0x100);
	}
}
void delete(){
	puts("which note do you wanna delete?");
	printf(">");
	int i= readint();
	if(i >= 0 && i<0x10)
	{
		free(array[i]);
		array[i]=0;
	}
}
void check()
{
	if(FLAG==0xcafebabe)
		system("/bin/sh\0");
	else
		printf("Byebye\n");
}
void init()
{
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	setvbuf(stderr,0,2,0);
}
int main()
{
	init();
	printf("The address of MAGIC_FLAG is %p, could you get it?\n",&FLAG);
	while(1)
	{
		menu();
		int cmd=readint();
		if(cmd==1)
			add();
		else if(cmd==2)
			delete();
		// else if(cmd==3)
		// 	edit();
		else
			break;
	}
	check();
}
