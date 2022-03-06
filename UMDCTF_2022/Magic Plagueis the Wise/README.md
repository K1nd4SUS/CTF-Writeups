# Magic Plagueis the Wise

## Description

Did you ever hear the tragedy of Darth Plagueis The Wise? It's written here in a magical way, but I can't figure out how to read it. Can you help me?

https://drive.google.com/file/d/1Yq5ckdzTmoUEnsyLzMJYTKLdz7JEw_ve/view?usp=sharing

## Solution

The zip contains 4464 different files

After some analisys seems that the only difference and important part is the first byte

Let's write e script to extract all these bytes and decode them

```python
text = []

for k in range(4465):
    with open(f"{k}", "rb") as f:
        text.append(f.read(1).decode())
print(''.join(text))
```

```console
$ python decode.py 
Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so
powerful and so wise he could use the Force to influence the midichlorians to create life. He
had such a knowledge of the dark side that he could even keep the ones he cared about from
dying. The dark side of the Force is a pathway to many abilities some consider to be
unnatural. He became so powerful. The only thing he was afraid of was losing his power, which
eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep. Ironic. He could save others from death, but
not himself.
Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so
powerful and so wise he could use the Force to influence the midichlorians to create life. He
had such a knowledge of the dark side that he could even keep the ones he cared about from 
dying. The dark side of the Force is a pathway to many abilities some consider to be
unnatural. He became so powerful. The only thing he was afraid of was losing his power, which
eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep. Ironic. He could save others from death, but 
not himself.
Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so
powerful and so wise he could use the Force to influence the midichlorians to create life. He
had such a knowledge of the dark side that he could even keep the ones he cared about from 
dying. The dark side of the Force is a pathway to many abilities some consider to be
unnatural. He became so powerful. The only thing he was afraid of was losing his power, which
eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep. Ironic. He could save others from death, but 
not himself.
Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so
powerful and so wise he could use the Force to influence the midichlorians to create life. He
had such a knowledge of the dark side that he could even keep the ones he cared about from 
dying. The dark side of the Force is a pathway to many abilities some consider to be
unnatural. He became so powerful. The only thing he was afraid of was losing his power, which
eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep. Ironic. He could save others from death, but 
not himself.

UMDCTF{d4r7h_pl46u315_w45_m461c}

Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. a Dark Lord of 
the Sith, so powerful and so wise he could use the Force to influence the midichlorians to 
create life. He had such a knowledge of the dark side that he could even keep the ones he
cared about from dying. The dark side of the Force is a pathway to many abilities some
consider to be unnatural. He became so powerful. The only thing he was afraid of was losing
his power, which eventually, of course, he did. Unfortunately, he taught his apprentice
everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others
from death, but not himself.
Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the
Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so
powerful and so wise he could use the Force to influence the midichlorians to create life. He
had such a knowledge of the dark side that he could even keep the ones he cared about from
dying. The dark side of the Force is a pathway to many abilities some consider to be
unnatural. He became so powerful. The only thing he was afraid of was losing his power, which
eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep. Ironic. He could save others from death, but
not himself.
```

#### **FLAG >>** `UMDCTF{d4r7h_pl46u315_w45_m461c}`