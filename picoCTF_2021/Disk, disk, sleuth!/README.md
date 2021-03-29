# Disk, disk, sleuth!

###### Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](dds1-alpine.flag.img.gz)

Idk why but i had some problem with `srch_strings`, so i tried with the old `strings`, filtering the result given the dimension of the file

```console
$ gzip -d dds1-alpine.flag.img.gz
$ strings dds1-alpine.flag.img | grep picoCTF
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_267e38f6}
```

#### **FLAG >>** `picoCTF{f0r3ns1c4t0r_n30phyt3_267e38f6}`