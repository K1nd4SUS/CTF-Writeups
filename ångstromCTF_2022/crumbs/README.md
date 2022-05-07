# crumbs

## Description

Follow the [crumbs](https://crumbs.web.actf.co/).

Server: [index.js](index.js)

## Solution

```python
from pwn import *
import requests

r = requests.Session()

s = r.get("https://crumbs.web.actf.co/")
print(f"status {s.status_code} - text {s.text}")

for i in range(1001):
    s = r.get(f"https://crumbs.web.actf.co/{s.text.split(' ')[2]}")
    #print(f"{i}> status {s.status_code} - text {s.text}")

s = r.get(f"https://crumbs.web.actf.co/flag")
print(f"{i}> status {s.status_code} - text {s.text}")
```

```
998> status 200 - text Go to 859f30d6-8dee-46bd-9690-4454ec32bee3
999> status 200 - text Go to 0f91fd8b-9546-445b-80f4-86405ddff9a0
1000> status 200 - text actf{w4ke_up_to_th3_m0on_6bdc10d7c6d5}
1000> status 200 - text Broke the trail of crumbs...
```

#### **FLAG >>** `actf{w4ke_up_to_th3_m0on_6bdc10d7c6d5}`