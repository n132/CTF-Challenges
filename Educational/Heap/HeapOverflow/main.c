#include<stdio.h>
char *          note_list[0x10] ={0};
unsigned int    note_len[0x10]  ={0};
void add()
{
    int idx = 0;
    puts("IDX");
    idx = getnum();
    if(idx>=0 && idx <0x10)
    {
        if(!note_list[idx])
        {
            puts("Size");
            unsigned int size = getnum();
            if(size < 0x4000)
            {
                char* res = malloc(size);
                if((long long)res<=0)
                {
                   exit(-1); 
                }
                note_len[idx]=size;
                return;
            }
            
        }
    }
    exit(-1);
    
}
void edit()
{
    int idx = 0;
    idx = getnum();
    if(idx>=0 && idx <0x10)
    {
        if(!note_list[idx])
        {
            unsigned int size = note_len[idx];
            readn(size,note_list[idx]);
        }
    }
    exit(-1);
}
void show()
{
    int idx = 0;
    idx = getnum();
    if(idx>=0 && idx <0x10)
    {
        if(note_list[idx])
        {
            write(1,note_list[idx],note_len[idx]);
        }
    }
    return;
}
void del()
{
    int idx = 0;
    idx = getnum();
    if(idx>=0 && idx <0x10)
    {
        if(note_list[idx])
        {
            free(note_list[idx]);
            note_list[idx]=0;
            note_len[idx]=0;
        }
    }
    return;
}
void menu()
{
    puts("++++++++++++++++");
    puts("    HOW2HEAP  ");
    puts("++++++++++++++++");
    puts("1. ADD  a note");
    puts("2. Edit a note");
    puts("3. Show a note");
    puts("4. Del  a note");
    
}
void readn(unsigned size,char *buf)
{
    if(size==0 || buf==0)
    {
        exit(1);
    }
    else
    {
        int res = read(0,buf,size);
        if(res<=0)
        {
            exit(1);
        }
    }
    return ;
}
int getnum()
{
    char buf[0x10]={0};
    puts("> ");
    readn(0xf,buf);
    return atoi(buf);
}
void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}
int main()
{
    init();
    while(1){
        menu();
        switch(getnum())
        {
            case 1:
            add(); break;
            case 2:
            edit(); break;
            case 3:
            show(); break;
            case 4:
            del(); break;
            default:
            exit(1);
        }
    }
}
