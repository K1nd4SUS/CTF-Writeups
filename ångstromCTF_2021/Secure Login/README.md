# Secure Login

## Description

My login is, potentially, and I don't say this lightly, if you know me you know that's the truth, it's truly, and no this isn't snake oil, this is, no joke, the most secure login service in the world (source).

Try to hack me at /problems/2021/secure_login on the shell server.

## Solution

Let's take a look to the code:


The function fgets, doesn't seem vulnerable... But strcmp starts comparing the first character of each string. If they are equal to each other, it continues with the following pairs until the characters differ or until a terminating null-character is reached. 
So if the two strings starts with the string terminator the function will return 0 because the two strings match up to the null character.

We reach our goal! Let's write the script:



#### **FLAG >>** `FLAG QUI`