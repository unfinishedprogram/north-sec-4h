# Friday May 19th
# Challenge attempt 1 (Electronic ties)
### Hints
- The first hint that I received of this challenge is that we received an electronic tie and that it had a USB port on the side of it, 
- ![[Pasted image 20230528102712.png]]
- Since the theme of this CTF was a dystopian corporate I assumed that all the ways of entering into given equipment were valid (we latter see in the challenges page of the website that it is a challenge to solve)

### Steps to resolve
1. How to even start connecting to the tie?
	- the first hint that we see on the tie is that we can probably with the USB using a computer
	- Looking at the chip on it (ESP32 chip) I searched it's name on google and realized that it's  chip chip commonly used for arduino that  could be connected with an application that uses a serial port (like putty).
	- I downloaded putty and set the right settings for connecting to it with the serial port (115200 for speed of the baud rate)
2. What to do after connecting?
	- After connecting to it i see that it is a sort of terminal with 3 commands (trying to type help shows this)
	- ![[Pasted image 20230528103853.png]]
	- After testing out that the few commands I realize that the most likely next step is to connect to the tie with Bluetooth
3. Bluetooth hints
	- I download an application on my phone that allows me to connect to ble devices (bluetooth low energy) however i fail to recognize or even find one tie on the network
	- After trying this same challenge at home (with less bluetooth devices around) i also fail to find this device on the bluetooth network
4. What was the last trail?
	- After giving up and coming back to this challenge multiple times, I realize that it's not worth solving because it's taking too much time
	- the last hint before going cold is that there is a soldering station in the convention room to add addons to our ties, I think there is a bluetooth antenna pin that I could have connected to the tie for it to become available in the bluetooth network
	
### After CTF hints
After the CTF was over we got a few hints about this tie
- It was a challenge that wasn't solved many times and that nobody got all of the points in the tie (the highest was 7 out of 15 points that are available)
- one of the 