# Revex

## Descrizione

As an active reddit user, clam frequently browses r/ProgrammerHumor. However, the reposts about how hard regex is makes him go >:((((. So, clam decided to show them who's boss.

`^(?=.*re)(?=.{21}[^_]{4}\}$)(?=.{14}b[^_]{2})(?=.{8}[C-L])(?=.{8}[B-F])(?=.{8}[^B-DF])(?=.{7}G(?<pepega>..).{7}t\k<pepega>)(?=.*u[^z].$)(?=.{11}(?<pepeega>[13])s.{2}(?!\k<pepeega>)[13]s)(?=.*_.{2}_)(?=actf\{)(?=.{21}[p-t])(?=.*1.*3)(?=.{20}(?=.*u)(?=.*y)(?=.*z)(?=.*q)(?=.*_))(?=.*Ex)`

## Soluzione

Abbiamo una regex e dobbiamo trovare una stringa che la soddisfi.

La regex è formata da diversi "blocchi" che devono essere tutti soddisfatti, possiamo inserire la regex su [regex101.com](https://regex101.com/) e analizzare un blocco alla volta aggiornando man mano la soluzione parziale.

Al termine otteniamo un'unica soluzione.

#### **FLAG >>** `actf{reGEx_1s_b3stEx_qzuy}`
