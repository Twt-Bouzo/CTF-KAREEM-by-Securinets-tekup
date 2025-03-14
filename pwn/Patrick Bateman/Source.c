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

