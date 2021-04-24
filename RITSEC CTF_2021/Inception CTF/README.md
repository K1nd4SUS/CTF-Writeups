# Inception CTF: Dream 1

## Description

The purpose of this CTF challenge is to identify common methods of hiding malicious files and code. In most cases adversaries will attempt to evade defenses in many cases by masquerading, hiding files, and more. There are five directories like the five levels in the movie Inception, Reality -> Van Chase -> The Hotel -> Snow Fortress -> Limbo. You will find one flag in each of the levels, that flag will also be the password to extract the next directory. Requirements: • You must have 7zip installed • Drop the InceptionCTF.7z on the Desktop as “InceptionCTF” • Use the option “Extract to "<name of directory>\” for the CTF to function properly Missing either of the above may result in complications which may cause issues when attempting to find flags.

NOTE: These challenges have a flag format of RITSEC{}

Dream 1: We have to get to their subconscious first, look for a hidden text file within the directory “Reality” this flag will unlock the next directory.

[InceptionCTFRITSEC.7z](InceptionCTFRITSEC.7z)

## Solution

In the first zip we found a hidden text file containing this:

```
Wait a minute, whose subconscious are we going into, exactly? {dnalmaerD}CESTIR
```

#### **FLAG >>** `RITSEC{Dreamland}`

# Inception CTF: Dream 2

## Description

Unfortunately, the subconscious isn’t enough for this mission, we have to kidnap Fischer we need to go further into the system of the mind. Use the flag found to edit the PowerShell script, entering the Flag in line three in-between the single quotes. Run the PowerShell script and wait for it to complete its actions.

## Solution

Ther is a hidden file containing this:

```
An idea is like a virus, resilient, highly contagious. 
52 49 54 53 45 43 7b 57 61 74 65 72 55 6e 64 65 72 54 68 65 42 72 69 64 67 65 7d
```

If we [deconde](https://gchq.github.io/CyberChef/#recipe=From_Hex('Space')&input=NTIgNDkgNTQgNTMgNDUgNDMgN2IgNTcgNjEgNzQgNjUgNzIgNTUgNmUgNjQgNjUgNzIgNTQgNjggNjUgNDIgNzIgNjkgNjQgNjcgNjUgN2Q) from HEX

#### **FLAG >>** `RITSEC{WaterUnderTheBridge}`

# Inception CTF: Dream 3

## Description

While the first two steps were easy it’s all hard from here on out, ThePointMan is the most crucial role of the mission he has to be presentable but without giving away our intentions. Use Alternate Dream State to find the flag before the kick.

## Solution

We get this file:

```
Q3JlYXRlIGEgbWF6ZSBpbiB0d28gbWludXRlcyB0aGF0IHRha2VzIG1lIG9uZSBtdW5pdGUgdG8gc29sdmUuIA==

59 6f 75 27 72 65 20 77 61 69 74 69 6e 67 20 66 6f 72 20 61 20 74 72 61 69 6e 2c 20 61 20 74 72 61 69 6e 20 74 68 61 74 20 77 69 6c 6c 20 74 61 6b 65 20 79 6f 75 20 66 61 72 20 61 77 61 79 2e 20 59 6f 75 20 6b 6e 6f 77 20 77 68 65 72 65 20 79 6f 75 20 68 6f 70 65 20 74 68 69 73 20 74 72 61 69 6e 20 77 69 6c 6c 20 74 61 6b 65 20 79 6f 75 2c 20 62 75 74 20 79 6f 75 20 63 61 6e 27 74 20 62 65 20 73 75 72 65 2e 20 62 75 74 20 69 74 20 64 6f 65 73 6e 27 74 20 6d 61 74 74 65 72 20 2d 20 62 65 63 61 75 73 65 20 77 65 27 6c 6c 20 62 65 20 74 6f 67 65 74 68 65 72 2e 20

|JP.HPVK.Q.G@.DCWDLA.QJ.AW@DH.GLBB@W	.aDWILKB. BXOR 25

Gung znal qernzf jvguva qernzf vf gbb hafgnoyr!

--. ..- .-.
..-. .-. .-. --.-
--. ..- -. --.
.--- .-.
-.-. -.-- -. .- --. .-. --.-
...- .-
--. ..- ...- ..-.
--.. -. .- .----. ..-.
--.. ...- .- --.-
--.. -. .-..
.--. ..- -. .- - .-.
.-. .. .-. . .-.. --. ..- ...- .- - .-.-.-

No place for a tourist in this job.
```

By decoding the various lines we get this (idk wht the 3rd is)

```
Create a maze in two minutes that takes me one munite to solve. 

You're waiting for a train, a train that will take you far away. You know where you hope this train will take you, but you can't be sure. but it doesn't matter - because we'll be together. 

That many dreams within dreams is too unstable!

THE SEED THAT WE PLANTED IN THIS MAN'S MIND MAY CHANGE EVERYTHING.
```

There is alse another file with no name

```
You mean, a dream within a dream? NTIgNDkgNTQgNTMgNDUgNDMgN2IgNDYgNDAgMjEgMjEgNjkgNmUgNjcgNDUgNmMgNjUgNzYgNDAgNzQgNmYgNzIgN2Q=

```

Let's [decode](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)From_Hex('Auto')&input=TlRJZ05Ea2dOVFFnTlRNZ05EVWdORE1nTjJJZ05EWWdOREFnTWpFZ01qRWdOamtnTm1VZ05qY2dORFVnTm1NZ05qVWdOellnTkRBZ056UWdObVlnTnpJZ04yUT0) it


#### **FLAG >>** `RITSEC{F@!!ingElev@tor}`