# information
###### Files can always be changed in a secret way. Can you find the flag? [cat.jpg](cat.jpg)
###### Make sure to submit the flag as picoCTF{XXXXX}

First thigh to note is that the flag to find is not he in standard way, now we can start to solve that challenge

Like always i start with a `strings` to see if there something interesting in the text of the file

```console
$ strings cat.jpg
JFIF
0Photoshop 3.0
8BIM
PicoCTF
http://ns.adobe.com/xap/1.0/
<?xpacket begin='
' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Image::ExifTool 10.80'>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
 <rdf:Description rdf:about=''
  xmlns:cc='http://creativecommons.org/ns#'>
  <cc:license rdf:resource='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/>
 </rdf:Description>
 <rdf:Description rdf:about=''
  xmlns:dc='http://purl.org/dc/elements/1.1/'>
  <dc:rights>
   <rdf:Alt>
    <rdf:li xml:lang='x-default'>PicoCTF</rdf:li>
   </rdf:Alt>
  </dc:rights>
 </rdf:Description>
</rdf:RDF>
</x:xmpmeta>
```
There are 2 lines the seems to contain something

`' id='W5M0MpCehiHzreSzNTczkc9d'?>`

`  <cc:licenserdf:resource='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/>`

The first one is not useful

The second one have the `resource` that seem like is encoded in Base64, let's try to decode it

```python
>>> import base64
>>> string = "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"
>>> base64.b64decode(string)
b'picoCTF{the_m3tadata_1s_modified}'
```

#### **FLAG >>** `picoCTF{the_m3tadata_1s_modified}`