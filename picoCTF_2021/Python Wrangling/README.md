# Python Wrangling
###### Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](ende.py) using [this password](pw.txt) to get [the flag](flag.txt.en)?

Another tutorial style challenge, lets run the file to see what happen

```console
$ python ./ende.py
Usage: ./ende.py (-e/-d) [file]
```

There's no need to check the code, it is logical that `-e` is for encryption and `-d` if for decryption

```console
$ python ./ende.py -d flag.txt.en
Please enter the password: 
```
 The script ask for a password, we can use the one provided by the [file](pw.txt)

```console
$ python ./ende.py -d flag.txt.en
Please enter the password:6008014f6008014f6008014f6008014f
picoCTF{4p0110_1n_7h3_h0us3_6008014f}
```

#### **FLAG >>** `picoCTF{4p0110_1n_7h3_h0us3_6008014f}`