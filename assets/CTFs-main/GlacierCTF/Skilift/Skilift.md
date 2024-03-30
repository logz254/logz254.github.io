## Question
You arrive at the base station of a ski lift. Unfortunately for you, the lift is not in operation but you have to reach the next summit somehow. You enter the control room to find a control terminal with the words "Please input your key:"

author:mole99
File: top.v
## Solution
1. Check out the provided file.
2. Reading through the code, you realize that there are a series of operations performed on the input key to generate a lock signal. The operations are:

(i) Stage 1 takes the input key and performs a bitwise AND operation with 64'hF0F0F0F0F0F0F0F0.
(ii) Stage 2 performs a bitwise left shift (<<<) by 5 on the result of Stage 1.
(iii) Stage 3 performs a bitwise XOR (^) operation with the constant value "HACKERS!".
(iv) Stage 4 subtracts 12345678 from the result obtained in Stage 3.
(v) the lock output is determined by checking if tmp4 matches the value 64'h5443474D489DFDD3.

3. To solve this, you need to reverse the operations that are occuring.
4. Check out **solv.py**, it does this for you. On running the script, you get the input key i.e., 0xe0102030604060
5. Use the input key to get the flag.

![Alt text](solv.png)

Flag: gctf{V3r1log_ISnT_SO_H4rd_4fTer_4ll_!1!}


