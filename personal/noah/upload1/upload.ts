fetch("http://chal8.hackademy.ctf/upload1.php", {
    "headers": {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "en-US,en;q=0.6",
        "cache-control": "max-age=0",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryMHAMbpOGWqJE19Cl",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1"
    },
    "referrer": "http://chal8.hackademy.ctf/upload1.php",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "body": "------WebKitFormBoundaryMHAMbpOGWqJE19Cl\r\nContent-Disposition: form-data; name=\"file\"; filename=\"libgetout.so\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryMHAMbpOGWqJE19Cl\r\nContent-Disposition: form-data; name=\"submit\"\r\n\r\nUpload\r\n------WebKitFormBoundaryMHAMbpOGWqJE19Cl--\r\n",
    "method": "POST",
    "mode": "cors",
    "credentials": "omit"
});