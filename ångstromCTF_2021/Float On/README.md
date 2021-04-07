# Float On

## Descrizione

I cast my int into a double the other day, well nothing crashed, sometimes life's okay.

We'll all float on, anyway: [float_on.c](float_on.c).

Float on over to `/problems/2021/float_on` on the shell server, or connect with `nc shell.actf.co 21399`.

## Soluzione

Dobbiamo trovare dei numeri che soddisfino certe condizioni:

* **Condizione 1:** `x == -x` \
La soluzione è `0`.

* **Condizione 1:** `x != x` \
La soluzione è `NaN`.

* **Condizione 1:** `x + 1 == x && x * 2 == x` \
La soluzione è `inf`.

* **Condizione 1:** `x + 1 == x && x * 2 != x` \
La soluzione è `1e100`.

* **Condizione 1:** `(1 + x) - 1 != 1 + (x - 1)` \
La soluzione è `2^53`.

Al termine otteniamo la flag.

#### **FLAG >>** `actf{well_we'll_float_on,_big_points_are_on_the_way}`