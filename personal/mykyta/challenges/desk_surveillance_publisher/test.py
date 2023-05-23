#!/bin/env python

import base64
import re
import subprocess
import time

PASS = "What I'm trying to do is to maximise the probability of the future being better"

def press(key):
    subprocess.Popen(['xdotool', 'key', key])
    time.sleep(0.05)

# Run the command
NC = subprocess.Popen(['nc', '9000:ff:1ce:ff:216:3eff:fe8c:4a0c', '8000'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

NC.stdin.write(f'{PASS}\n'.encode())
NC.stdin.flush()
INTRO = NC.stdout.readline()
print(INTRO)

exit()
while True:
    # Get firmware
    FIRMWARE = NC.stdout.readline()
    try:
        FIRMWARE = base64.b64decode(FIRMWARE)
    except:
        print(FIRMWARE)
        exit()
    with open("./out", "wb") as f:
        f.write(FIRMWARE)

    # Open binary ninja
    NINJA = subprocess.Popen(['binaryninja-demo', './out'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    time.sleep(1)
    press('Enter')

    # Select main function code
    time.sleep(2.5)
    press('Down')
    for _ in range(57):
        press('Shift+Down')

    # Copy and get
    press('ctrl+c')

    CLIP = subprocess.Popen(['xsel', '--clipboard', '--output'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    CODE = "".join([c.decode() for c in CLIP.stdout.readlines()])

    time.sleep(0.1)
    CLIP.terminate()
    NINJA.terminate()

    # Parse
    COUNT_SCANF = len(re.findall(r'(scanf)', CODE))
    COUNT_STDIN = len(re.findall(r'(stdin)', CODE))
    ANSWER = [n for n in range(COUNT_SCANF)]
    ANSWER += ['./secret']
    ANSWER += ['\n' for n in range(COUNT_STDIN - 1)]
    ANSWER = '\n'.join([str(n) for n in ANSWER])
    print(ANSWER)
    ANSWER = base64.b64encode(ANSWER.encode())

    # Write codes
    NC.stdin.write(ANSWER + b'\n')
    NC.stdin.flush()

    NINJA.terminate()

    # Get output
    RESULT = NC.stdout.readline()
    print(RESULT)

    exit()

