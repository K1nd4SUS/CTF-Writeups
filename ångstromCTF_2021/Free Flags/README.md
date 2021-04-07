# FREE FLAGS!!1!! 

## Descrizione

Clam was browsing armstrongctf.com when suddenly a popup appeared saying "GET YOUR FREE FLAGS HERE!!!" along with a download. Can you fill out the survey for free flags?

Find it on the shell server at `/problems/2021/free_flags` or over netcat at `nc shell.actf.co 21703`.

## Soluzione

Dobbiamo rispondere a certe domande:

* **Domanda 1:** `What number am I thinking of???` \
Disassemblando l'eseguibile troviamo che la risposta è `31337`.

* **Domanda 2:** `What two numbers am I thinking of???` \
Disassemblando l'eseguibile troviamo che i numeri devono essere tali che la loro somma sia `1142` e il loro prodotto sia `302937`, si può trovare facilmente che i due numeri sono `419` e `723`.

* **Domanda 3:** `What animal am I thinking of???` \
Disassemblando l'eseguibile troviamo che la risposta è `banana`.

Al termine otteniamo la flag.

#### **FLAG >>** `actf{what_do_you_mean_bananas_arent_animals}`