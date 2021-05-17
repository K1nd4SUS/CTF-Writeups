# Tiny interpreter

## Description

We wrote an interpreter just so we can run our own binaries. Can you figure it out?

[interpreter](interpreter) \
[bin](bin)

## Solution

Let's try to run the interpreter

```console
$ chmod +x interpreter 
$ ./interpreter 
Usage:
./interpreter <program you want to run>
```

Ok, let's give the bin file as input

```
$ ./interpreter bin
I
n
t
e
r
p
r
e
t
e
r
_
w
r
i
t
t
e
n
_
i
n
_
C
_
i
s
_
a
_
g
r
e
a
t
_
i
d
e
a
```

#### **FLAG >>** `dctf{Interpreter_written_in_C_is_a_great_idea}`