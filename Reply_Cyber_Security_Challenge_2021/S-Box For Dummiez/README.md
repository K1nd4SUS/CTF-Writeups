# S-Box For Dummiez

## Description

Reunited at the Temple of Nebula, the Five Legends and R-Boy prepare their final attack.

[misc100-readme](misc100-readme.pdf)

## Solution
Pass 000000000 into the circuit and take note of the output. Pass the output as input to the circuit. Repeat 10 times. Use the 10 outputs as indexes in the map and obtain the flag's characters.
```
bin		hex	char
000000000       0x000
000010000       0x010   w
000011000       0x018   e
000010101       0x015   e
101110101       0x175   G
100110011       0x133   o
100111011       0x13B   0
100110110       0x136   d
001000110       0x046   Y
000011101       0x01D   0
101111101       0x17D   u
```

#### **FLAG >>** `{FLG:weeGo0dY0u}`
