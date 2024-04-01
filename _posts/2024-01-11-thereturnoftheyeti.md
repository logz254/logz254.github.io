---
layout: post
title: TheReturnoftheYeti
date: 2024-01-11 22:53 +0300
categories: [TryHackMe, Advent of Cyber (AoC) 2023 Side Quest]
tags: [aoc,tryhackme,wirehack,forensics,aircrack-ng,wpa,cyberchef,pyrdp-player]
---
## Introduction
Every year, TryHackMe hosts Advent of Cyber event. During this event, several fields of cybersecurity are covered through solving tasks. The event is aimed at beginners though anyone with an interest in cybersecurity can learn and benefit immensely from it.

Also, another set of tasks called Advent of Cyber Side Quests which are meant for intermediate individuals and beyond. Today, we'll cover the first one since I was able to solve most of it.

# Category: Forensics

![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/overview.png)


## What's the name of the WiFi network in the PCAP?

First step is to download the required file which is in a zip format. On unzipping, you are presented with VanSpy.pcapng.So this is a new generation packet capture file and it immediately tells you that WireShark is involved.

Firing up Wireshark, I'm presented with the following
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/encrypted_packets.png)

Scrolling to the end of any packet, you get the name of the WiFi network which is the value of the SSID i.e., FreeWifiBFC
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/solv_1.png)


## What's the password to access the WiFi network?

Based of scrolling through all the captured packets, you realize that they are encrypted and needed to find a way to decrypt them. After carrying out some research, I came across this page from HackTricks (https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/wifi-pcap-analysis)

![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/hacktrics_idea.png)

In my case, it will be:

aircrack-ng -w /usr/share/wordlists/rockyou.txt -b 22:c7:12:c7:e2:35 VanSpy2.pcap

Here is a breakdown of the cases, I chose rockyou are the wordlist since it is commonly used. BBSID is shown below:
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/bbsid.png)

I tried running it the command using the original file i.e., aircrack-ng -w /usr/share/wordlists/rockyou.txt -b 22:c7:12:c7:e2:35 VanSpy.pcapng, but aircrack-ng doesn't support this file type.

By running the command, we get the password to access the WiFi network
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/solv_2.png)


## What suspicious tool is used by the attacker to extract a juicy file from the server?

Use the password as shown below to decrypt the packets
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/decryption_keys.png)

You should be able to see the packets with different protocols.

Inspecting random TCP packets didn't yield much fruit until I decided to filter the packets by Length in descending order.
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/descending_packets.png)

Following the TCP stream of the first packet, we get some juicy information. I've picked the below image since it captures the main part of what the malicious actor achieved.
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/juicy_info.png)

So the actor was able to gain access to the Windows machine and to their advantage, the account was an administrator account i.e., whoami command. He/she downloaded a common credentials harvesting tool called Mimikatz from its github repository and output the files as mimi.zip. The actor extracted the contents into the current directory i.e., C:/Users/Administrator

The actor then ran mimikatz to export the Remote Desktop Certificate and finally to encode the contents of the exported certificate to base64 as shown below.
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/juicy_info2.png)


![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/solv_3.png)

Note: I was able to reach this point of the challenge during the time allocated. Beyond here, its more of research.

## What is the case number assigned by the CyberPolice to the issues reported by McSkidy?

Decoding the certificate using CyberChef and saving it as .pfx, we get the certificate.
Digging around, I came across this site: https://www.ibm.com/docs/en/arl/9.7?topic=certification-extracting-certificate-keys-from-pfx-file which helped to extract the decoded key.

So first, you extract the private key
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/encrypted_key.png)

By default, when running mimikatz to export the certificate, the password used is mimikatz. So use that password when prompted for "Enter Import Password:", "Enter PEM pass phrase:" and "Verifying - Enter PEM pass phrase:"

Then decrypt the private key
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/decrypting_private_key.png)

Once again, when prompted for the pass phrase, key in mimikatz.
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/decrypted_private_key.png)

Ensure you add the key to the pcap file as shown.
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/add_private_key.png)


# Note: I was able to reach this point of the challenge during the time allocated. Beyond here, it's more of research from released writeups

Digging around, I released the key for the last two challenges was right infront of me but making sense of the RDP packets was the issue.
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/gibberish.png)

To get a better understanding of what went on, we can "replay" the RDP session using this tool:https://github.com/GoSecure/pyrdp. Follow the provided instructions on how to install it on your VM.

To use it, first we convert the pcap file to pyrdp file. To avoid the many errors, just rename VanSpy2.cap to rdp.pcap
![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/pyrdp_convert.png)

Then run pyrdp-player ./20231125145052_10.0.0.2:55510-10.1.1.1:3389.pyrdp where ./20231125145052_10.0.0.2:55510-10.1.1.1:3389.pyrdp is the resulting regenerated file. Now you can kick back, relax and enjoy the show.

![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/solv_4.png)


## What is the content of the yetikey1.txt file?

![Alt text](/assets/CTFs-main/TheReturnoftheYeti/TheReturnoftheYeti/solv_5.png)

That's all for now. Cheers

