# Weird File

###### What could go wrong if we let Word documents run programs? (aka "in-the-clear"). [Download file](weird.docm).

It's a Microsoft Word file that contain also macros, so let's try to open it and find what this macros do

![windows macro screen](img1.png)

This line seems to contain something, probably a Base64 encoded text

`Ret_Val = Shell("python -c 'print(\"cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9\")'" & " " & Args, vbNormalFocus)`

```python
>>> import base64
>>> text = "cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9"
>>> base64.b64decode(text)
b'picoCTF{m4cr0s_r_d4ng3r0us}'
```

#### **FLAG >>** `picoCTF{m4cr0s_r_d4ng3r0us}`