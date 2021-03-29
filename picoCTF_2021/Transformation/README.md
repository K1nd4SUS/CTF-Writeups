# Transformation

###### I wonder what this really is... [enc](enc) ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

Before analyze the code, let's open the file and see if it contains something that i can use to understand more the type of encode

```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽
```

Maybe [converting](https://www.rapidtables.com/convert/number/ascii-to-hex.html) one character from ascii to hex can explain more...

```
灩 > 7069
```

This 4 digit number seems like 2 hex code, let's try to [decode](https://www.rapidtables.com/convert/number/hex-to-ascii.html) it

```
7069 > pi
```

This `pi` remind me of the `picoCTF{}` flag format, so i think i have found the solution, just try with the other characters and see what happen

```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽
7069 636f 4354 467b 3136 5f62 6974 735f 696e 7374 3334 645f 6f66 5f38 5f65 3134 3161 3066 377d
```
```
7069 636f 4354 467b 3136 5f62 6974 735f 696e 7374 3334 645f 6f66 5f38 5f65 3134 3161 3066 377d
picoCTF{16_bits_inst34d_of_8_e141a0f7}
```
#### **FLAG >>** `picoCTF{16_bits_inst34d_of_8_e141a0f7}`