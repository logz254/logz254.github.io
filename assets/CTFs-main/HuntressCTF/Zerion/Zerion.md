## Question
Author: @JohnHammond

We observed some odd network traffic, and found this file on our web server... can you find the strange domains that our systems are reaching out to?

NOTE, this challenge is based off of a real malware sample. We have done our best to "defang" the code, but out of abudance of caution it is strongly encouraged you only analyze this inside of a virtual environment separate from any production devices.

## Solution
Credit to **Pr0f_41bu5** for helping to solve this challenge.

Upload the malware to CyberChef.
![Alt text](cyberchef.png)

We will be using two operations to get the flag, first we use **Reverse** Operation to reverse the input string:
![Alt text](reverse.png)

Then **From Base64** Operation to decode data from an ASCII Base64 string back into its raw format. Under the Alphabet option, use ROT13:
![Alt text](flag.png)


flag{af10370d485952897d5183aa09e19883}