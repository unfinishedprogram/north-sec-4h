#!/bin/env python

import subprocess
import base64

# Run the command
NC = subprocess.Popen(['nc', '9000:ff:1ce:ff:216:3eff:fe8c:4a0c', '8000'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

NC.stdin.write(b'I have come for the shadow training\n')
NC.stdin.flush()
NC.stdout.readline()

while True:
    # Get firmware
    FIRMWARE = base64.b64decode(NC.stdout.readline())
    with open("./out", "wb") as f:
        f.write(FIRMWARE)

    # Get codes
    NINJA = subprocess.Popen(['binaryninja-demo', './out'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    CODES = []
    for i in range(5):
        NUMBER = input()
        CODES.append(int(NUMBER, 16))
    CODES = '\n'.join([str(c) for c in CODES])
    CODES = base64.b64encode(CODES.encode())

    # Write codes
    NC.stdin.write(CODES + b'\n')
    NC.stdin.flush()

    NINJA.terminate()

    # Get output
    RESULT = NC.stdout.readline()
    print(RESULT)
