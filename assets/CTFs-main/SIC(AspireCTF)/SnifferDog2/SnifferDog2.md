## Question
What is the 6th disallowed item listed in http://192.168.56.103:8081/robots.txt?

## Solution
Use this display filter: "ip.addr == 192.168.56.103 and tcp.port == 8081". This tells Wireshark to filter out packets containing ip addresses that are not 192.168.56.103 and ports that are not 8081.

Scroll through packets until you arrive at a packet that is requesting for robots.txt i.e. GET /robots.txt HTTP/1.1 or No.2288
![Alt text](packets.png)

Right click the packet and Follow the TCP stream
![Alt text](tcp_stream.png)

SHCTF{installation}
