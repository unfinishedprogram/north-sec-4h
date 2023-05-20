Annual Review

AWS server
serving files
  -preview.php
    network request file=/var/www/html/guide.md
  -app.php
  -index.php

Are trying to find what the file hierarchy is.
running gobuster didn't work can't ping

requested /preview.php?file=/var/www/html/preview.php got this:
```php
<?php
  require_once('libs/utils.php');

  if (!is_auth())
    redirect('index.php');

  $file = $_GET['file'];
  if (isset($file)) {
    header("Content-Type: text/plain");
    echo get_file($file);
  }
?>
```
previewed libs/utils.php which mentionned libs/dynamo.php
The flag was inside of there: flag-d19650aa911acb7c130aa380601d169d3bd08ab4

---

Part 2 
Need to find HR credentials

Dynamo.php contains AWS key and secret
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Using.API.html 

Installed AWS CLI
logged into aws CLI with credentials found in dynamo.php
aws dynamodb scan --table-name "GOD_LoginEmployee"
found flag as password.

---

Part 3

With the HR credentials we logged in as HR

There was a url to some documentation which contained the flag

---