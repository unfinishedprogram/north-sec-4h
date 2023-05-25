# Mykyta Onipchenko

## Upload 1

This challenge required to exploit a image upload form to trick it to execute a `.php` file. There
was even a hint in the comment in the source code of the page. So, I created a simple `.php` file:

```php
<?php
    echo "<h1>Hello</h1>"
?>
```

I tried uploading it as is, but it complained about file extension not being `.png` or `.jpg`. So I
reuploaded the file with `.png` extension and it uploaded correctly, but I still didn't get a flag.
I looked further into source code of the page, and turns out the form is for a generic file upload,
and the file type is probably verified server-side with regex on the file name. So I uploaded the
file with extension `.png.php`, and got the flag.

## Upload 2

This challenge builds on top of the previous challenge by providing extra validation for file
upload. Reuploading the same file didn't work. I looked into the post request I'm sending when
uploading the file, and it showed that the filetype is `application/php`. I looked into which
software will let me edit the post request and installed Burp Suite. After changing the filetype to
`image/png`, I got the flag.

## Upload 3

This challenge also adds a new validation. I assumed next step would be to change magic bytes of
the file. A quick google search after I found what is the file signature of the png file, inserted
it before php code, and uploaded the file.

## Upload 4

I was stuck on this one for a while. Uploading the file gave me an error message "uploading `.php`
file is not allowed because we are tired of getting hacked". I looked further in how I can spoof
the file format, and I found that inserting a null byte between double file extensions might work
because some languages expect strings to be null terminated and won't read past the null byte. But
it didn't work. But after some experimentation, I found out that I only needed to change file
extension to `.png.php5`.

## Desk surveillance publisher - 1

The instructions had a password and a command

```bash
nc 9000:ff:1ce:ff:216:3eff:fe8c:4a0c 8000
```

After running the command and typing it the password, I received instructions to send security
codes and some long base 64 string. Decrypting it gave me a binary file which requests 5 passwords.
Luckily, they were hard coded in the executable in a comparison, so extracting them wasn't an
issue. So I ran `nc` command again and tried submitting the codes, but it didn't work, even if they
were correct. I was stuck for a while here and even opened a support ticket. Turns out the command
sends a unique executable every time and gives a 30 second time limit to submit the code. So I
made a script to automatically fetch a new executable and to open my disassembly software (Binary
Ninja), so I can copy and paste the codes. It worked, but it requested another set of codes. I
wrapped everything in a while loop, but it requested new codes again and again. I tried exploring
python libraries to disassemble, but I couldn't figure our where the passwords were hard coded.
Binary Ninja simplifies the code and writes it in a pseudo C.

Next day, I gave it another shot. I still didn't understand assembly code, but I remembered about a
Linux utility `xdotool` which lets me send key presses to the app. My unconventional solution was
to open Binary Ninja, send key presses to select and copy main function in pseudo C, parse it using
regex and send the codes. Surprisingly, it worked. After around 20 binaries, it sent me a flag.
Funnily enough it sent it in place of the message with the binary, so my app crashed when trying to
decode it as wasn't a valid base64 string. So I hastily updated my macro with a try catch block and
it finally worked.

## Desk surveillance publisher - 2

I also received a new password to use with the old `nc` command. The format of the binary changed,
there was a new validation for a system file so I could not run it on my computer. The passwords
were still hard coded, I only needed to update my regex a bit to make it work with the new format.
