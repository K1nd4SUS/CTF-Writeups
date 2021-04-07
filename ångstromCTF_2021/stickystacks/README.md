# stickystacks

## Descrizione

I made a program that holds a lot of secrets... maybe even a flag!

[Source](source.c)

Connect with `nc shell.actf.co 21820`, or visit `/problems/2021/stickystacks` on the shell server.

## Soluzione

Notiamo subito che viene chiamata la funzione `printf` con una stringa letta dall'input, la stringa però deve essere al più di 5 caratteri.

Utilizzando la sinstassi `%42$p`, sostituendo l'indice, possiamo stampare buona parte dello stack. Convertendo i valori ottenuti da esadecimale possiamo ottenere la flag.

#### **FLAG >>** `actf{this_is_how_lockpicking_works_right}`