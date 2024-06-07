# spooftest by scramblr - Test IP Spoofing IPHM Server Without Self-Snitching To Caida!
Spooftest by SCRAMBLR is a small toolkit that can check IP Spoofing IPHM Capabilities of
your servers **WITHOUT HAVING TO SNITCH ON YOURSELF BY USING CAIDA TOOLS!**

June 7 2024:
- Added spooftest.py testing tool
- Updated documentation

Follow these simple instructions to test any server for IP Spoofing (IPHM IP Header Modification) capabilities instead of using the tool by CAIDA which
WILL ALMOST ALWAYS CAUSE YOUR PROVIDER TO BE HARASSED UNTIL THEY SHUT SPOOFING DOWN! Don't be dumb! Use these instructions!

Last Update: **JUNE 06 2024**
Created By: **SCRAMBLR** _(P4CK3T H4NDL3R)_

# ----[ Requirements to test for IP Spoofing ]----
# 1.) tcpdump Server: ANY server that can run tcpdump. 
_*Does not need to be able to spoof._

# 2.) Your IP Spoof (IPHM) Server
_Have "scapy" or "python-scapy" installed on it._

**----[ Setup Instructions For Both Machines ]----**

_On DEBIAN, UBUNTU, OR ANY APTITUDE BASED *NIX MACHINES:_
```
apt-get update
 
apt-get install net-tools bind9-dnsutils inetutils-tools tcpdump graphviz python3-scapy -y
 
apt-get install python3-scapy -y
```

_CENTOS, FEDORA, OR OTHER YUM BASED MACHINES:_
```
yum update
 
yum install tcpdump net-tools bind-utils python-pip -y
 
easy_install pip # dont worry if this one doesn't work.
 
pip install scapy _or_ pip3 install scapy
```

_RUNNING SOME OTHER WEIRD DISTRO, OR WANT TO INSTALL EVERYTHING VIA SOURCE? OK, HAVE FUN!_

**# ----[ End Install Instructions ]----**

# 3.) **# ----[ Running The Tests To Check For IP Spoofing ]----**

_Open an SSH/Terminal session to the host #1 (The tcpdump server) and begin running tcpdump by using the following command._

```
**# ====[ SERVER ONE ]====**
server1$ **sudo su -** _(You will need to run tcpdump as root.)_
server1# **tcpdump -i eth0 -nnv -c 5000 icmp**
```
This will run tcpdump and listen for up to 5,000 ICMP packets. You shouldn't be getting many ICMP packets until we run the next set of commands.

_NOTE: If you get error "tcpdump: eth0: No such device exists" <-- You will need to find the correct name of your interface, check 'ifconfig' or ip addr.
It's likely something similar to ens33 or ens33p1 or some other stupid name. :) Replace and try again._

**# ====[ SERVER TWO ]====**
Open another SSH/Terminal session to host #2 (The IP Spoofing Server) and run the following command.

_NOTE: Again, you must be root. Then, run:_
```
server2# **scapy**
```
After scapy loads, you'll paste the text below exactly, do not press enter..
```
**import random
def randomIP():
	ip = ".".join(map(str, (random.randint(0, 255)for _ in range(4))))
	return ip
send(IP(src=RandIP(),dst="**
```
After the dst=" you will paste in your tcpdump server's IP address (Server #1). Then, paste the rest of the code that follows:
```
**")/ICMP()/"SPOOFTESTICMP",count=5000)**
```
It should look like this if you did it right, for the 5th line:
```
send(IP(src=RandIP(),dst="**5.6.7.8**")/ICMP()/"SPOOFTESTICMP",count=5000)
```
But instead of 5.6.7.8 it will be Server #1's IP (The tcpdump server's IP). 

Hit enter, and it'll send 5,000 ICMP packets that SHOULD all come from random IP addresses to your tcpdump server. If nothing comes,
or if only one IP address shows up - chances are that your server cannot spoof IP addresses or that you (somehow) managed to screw
up these instructions. You should be ashamed. 

THATS IT. THATS ALL IT TAKES TO NOT SELF-SNITCH TO CAIDA ABOUT YOUR SHINY NEW IP SPOOF SERVER! In order to find this set of instructions
quick when you need them, just google "scramblr spoof 

