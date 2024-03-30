---
layout: post
title: SnifferDog3
date: 2023-09-24 16:15 +0300
categories: [SheHacks Intervarsity CTF, SnifferDog3]
---
## Question
What version of Jenkins is running on 192.168.56.103? shctf{VersionOnly}

## Solution
Display filter: "ip.addr == 192.168.56.103"
![Alt text](assets\CTFs-main\SIC(AspireCTF)\SnifferDog3\jenkins_packet.png)

Follow TCP stream of selected packet i.e. No.2181
![Alt text](assets\CTFs-main\SIC(AspireCTF)\SnifferDog3\tcp_stream.png)

Pay attention to "X-Jenkins: 1.647"

SHCTF{1.647}
