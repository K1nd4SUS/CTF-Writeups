# Mem-X

## Description

Do you ever find yourself forgetting about {mem_promo_list_rnd}? Well, you're not alone. That's why we created Mem-X, rigorously designed through hundreds of medical and psychological trials to be the perfect memory preservation system. You can find the Discord bot on the X-MAS CTF server, it is the Mem-X#0493 user.

Start your memory journey today with !help.

Hint: Flag is in /flag.txt

## Solution

First of all let's get the commands

```
!help

+ !note
   = !note [note text]     | make a new note! you will never forget it.

+ !remember
   = !remember [notehash]  | remember a note! you'll need the hash you got when you made it.
```

Let's create a note

```
!note test

Your note has been saved! Here's its hash: 5251b21a6eac7d9d7864170fe88cee37
Use that (!remember 5251b21a6eac7d9d7864170fe88cee37) to remember your note!
```

Let's try to get the flag

```
!remember flag

We couldn't find a note called flag.txt! :(
```

The answer is very interesting, let's try exactly what the description says

```
!remember /flag

Here's your note!
X-MAS{f0rgEtt1nG_EvEry7h1Ng_abf91b10e019c}
```

#### **FLAG >>** `X-MAS{f0rgEtt1nG_EvEry7h1Ng_abf91b10e019c}`