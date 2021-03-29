# It is my Birthday

###### I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website. http://mercury.picoctf.net:20277/

The site want 2 small PDF, if we try with some 400kB PDFs it return that they are to big. The second requirement is that the MD5 of the 2 files need to be the same. Fortunately we can find these file online (Thx [Corkami](https://github.com/corkami/collisions))

Let's try with [poeMD5_A](poeMD5_A.pdf) and [poeMD5_B](poeMD5_B.pdf)

```console
$ md5sum poeMD5_A.pdf poeMD5_B.pdf 
b347b04fac568905706c04f3ba4e221d  poeMD5_A.pdf
b347b04fac568905706c04f3ba4e221d  poeMD5_B.pdf
```

Excellent, the site redirect us to a new page where the flag is present 

```php
<?php

if (isset($_POST["submit"])) {
    $type1 = $_FILES["file1"]["type"];
    $type2 = $_FILES["file2"]["type"];
    $size1 = $_FILES["file1"]["size"];
    $size2 = $_FILES["file2"]["size"];
    $SIZE_LIMIT = 18 * 1024;

    if (($size1 < $SIZE_LIMIT) && ($size2 < $SIZE_LIMIT)) {
        if (($type1 == "application/pdf") && ($type2 == "application/pdf")) {
            $contents1 = file_get_contents($_FILES["file1"]["tmp_name"]);
            $contents2 = file_get_contents($_FILES["file2"]["tmp_name"]);

            if ($contents1 != $contents2) {
                if (md5_file($_FILES["file1"]["tmp_name"]) == md5_file($_FILES["file2"]["tmp_name"])) {
                    highlight_file("index.php");
                    die();
                } else {
                    echo "MD5 hashes do not match!";
                    die();
                }
            } else {
                echo "Files are not different!";
                die();
            }
        } else {
            echo "Not a PDF!";
            die();
        }
    } else {
        echo "File too large!";
        die();
    }
}

// FLAG: picoCTF{c0ngr4ts_u_r_1nv1t3d_da36cc1b}

?>
```

#### **FLAG >>** `picoCTF{c0ngr4ts_u_r_1nv1t3d_da36cc1b}`
