![image](https://github.com/user-attachments/assets/cd803c2a-5baa-4241-8c50-dae2181196ab)


First of all,Let's execute the program.

![image](https://github.com/user-attachments/assets/0f601582-6c0c-463e-8a44-72620f0da70c)

No, we are going to reverse the binary using a decompiler.

For me, I used IDA Pro.

The nature of this task is that it is implemented in C++, the code starts by accepting user input and encrypting it by XOR-ing each byte with 0x89. 

Specifically, for each index i, the following operation is performed:
enc[i]=input[i]^0x89

Next, the program stores a hard-coded flag into a buffer, named flag, using a series of 64-bit and one 32-bit assignments.

![image](https://github.com/user-attachments/assets/2b70ef3a-c0ff-4611-92a2-9291557d4de1)

On little-endian systems, the bytes in each constant are stored in reverse order.

the program compares the enc input  with the bytes stored in the flag.

Since the flag was stored as constants, we must account for the little-endian storage order.
0xECE7E0FBFCEAECDALL ------> DA, EC, EA, FC, FB, E0, E7, EC

0xBEB1BBB0ECF2FAFDLL ------> FD, FA, F2, EC, B0, BB, B1, BE

0xB1BBB8BDEABAEDBELL ------> BE, ED, BA, EA, BD, B8, BB, B1

0xEBBFBCBAB8EDEAEALL ------>  EA, EA, ED, B8, BA, BC, BF, EB

0xEFBCEDB8B9E8BABELL ------>  BE, BA, E8, B9, B8, ED, BC, EF

0xEFBABBBDBDBDBBBCLL ------>  BC, BB, BD, BD, BD, BB, BA, EF

0xB1BEBBEBBEBCBBEFLL ------>  EF, BB, BC, BE, EB, BB, BE, B1

Bytes 56–59 (from the 32-bit value –1162298690, which is 0xBAB8BABE in unsigned form) :

0xBAB8BABE ------> BE, BA, B8, BA

0xEABBEFBFEDB9BABCLL ------> BC, BA, B9, ED, BF, EF, BB, EA

0xF4ECEDB8B1EFB8BFL ------> BF, B8, EF, B1, B8, ED, EC, F4

Finaly, here is the solver code on python :

```Python
#koooll w wwakeel
flag_bytes = [
    0xECE7E0FBFCEAECDA,
    0xBEB1BBB0ECF2FAFD,
    0xB1BBB8BDEABAEDBE,
    0xEBBFBCBAB8EDEAEA,
    0xEFBCEDB8B9E8BABE,
    0xEFBABBBDBDBDBBBC,
    0xB1BEBBEBBEBCBBEF,
    -1162298690,  # 32-bit value
    0xEABBEFBFEDB9BABC,
    0xF4ECEDB8B1EFB8BF
]

flag = ""

def decrypt_flag_bytes(byte_value):
    byte_sequence = bytearray()
    for i in range(8):
        byte_sequence.append(byte_value & 0xFF)
        byte_value >>= 8
    return ''.join(chr(b ^ 0x89) for b in byte_sequence)

# Iterate over each 64-bit or 32-bit value
for value in flag_bytes:
    if value < 0:
        value += 2**32
    
    flag += decrypt_flag_bytes(value)

print(flag)
```

![image](https://github.com/user-attachments/assets/bda46264-b859-482c-b801-f7f71b23916e)

FLAG : Securinets{e92877d3c4128ccd1356b73a01d5f5244423ff257b2787313530d6f2c61f81de}

