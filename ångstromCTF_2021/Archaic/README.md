# Archaic

## Description 

The archaeological team at ångstromCTF has uncovered an archive from over 100 years ago! Can you read the contents?

Access the file at [/problems/2021/archaic/archive.tar.gz](archive.tar.gz) on the shell server.

## Solution

Just download the file, unarchive and see what happen

```console
$ tar -xvzf archive.tar.gz 
flag.txt
tar: flag.txt: implausibly old time stamp 1921-04-01 23:45:12
$ cat flag.txt 
cat: flag.txt: Permission denied
$ chmod +r flag.txt 
$ cat flag.txt 
actf{thou_hast_uncovered_ye_ol_fleg}
```

#### **FLAG >>** `actf{thou_hast_uncovered_ye_ol_fleg}`