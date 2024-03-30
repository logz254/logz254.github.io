---
layout: post
title: SnifferDog1
date: 2023-09-24 16:15 +0300
categories: [SheHacks Intervarsity CTF, SnifferDog1]
---
## Question
How many packets in total passed through port 445 shctf{Ans}
File: [snifferdog.pcap](/assets/CTFs-main/SIC(AspireCTF)/SnifferDog1/snifferdog.pcap)

## Solution
Open the file using Wireshark.
Use this display filter: "tcp.port == 445". This tells Wireshark to filter out packets that don't pass through port 445.

![Alt text](/assets/CTFs-main/SIC(AspireCTF)/SnifferDog1/packets.png)

Look at the bottom part of the Wireshark window and take note of the displayed packets i.e. "Displayed: 10638"

SHCTF{10638}