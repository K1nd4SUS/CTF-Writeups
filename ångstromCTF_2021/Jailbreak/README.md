# Jailbreak

## Descrizione

Clam was arguing with kmh about whether including 20 pyjails in a ctf is really a good idea, and kmh got fed up and locked clam in a jail with a python! Can you help clam escape?

Find it on the shell server at `/problems/2021/jailbreak` over over netcat at `nc shell.actf.co 21701`.

## Soluzione

Disassemblando l'eseguibile notiamo che per ottenere la flag dobbiamo soddisfare certe condizioni inserendo determinate stringhe, le stringhe sono in ordine:
* `pick the snake up`
* `throw the snake at kmh`
* `pry the bars open`
* `press the red button`
* `press the green button`
* `press the red button`
* `press the red button`
* `press the green button`
* `press the green button`
* `press the green button`
* `press the red button`
* `press the red button`
* `press the green button`
* `bananarama`

Al termine otteniamo la flag.

#### **FLAG >>** `actf{guess_kmh_still_has_unintended_solutions}`