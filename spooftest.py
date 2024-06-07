#!/usr/bin/python3
#
# spooftest.py version v1.2
# USAGE:
# server# chmod a+x spooftest.py
# server# ./spooftest.py <dest server> <num of packets to send>
#
#
# This is a small, simple script to test your server's abilities to spoof IPv4 packets or not.
# You should use this instead of things like caida project's tool, because they're rumored to
# collect data or hand it off to others who harass the server/network owners until they re-configure
# their networks and discontinue allowing spoofed packets.
#
# By default, this script sends spoofed packets to fuzzme.packet.tel - but it can be configured to
# send them anywhere. You can download a constantly running pcap by typing:
# wget http://fuzzme.packet.tel/fuzzme.packet.tel.last10minutes.pcap
# EDIT: packet.tel has been killed off for now, and also I think cock.li (my host) may be in some hot water,
# sooooo yeah. No fun utilities like fuzzme for now.
#
# Thank the White Knights of the Internet for all of this crap.
#
# Requires scapy and a spoofy box
#
# TO DO:
# - Remove sys calls because theyre lame
# - Fix the code to make it less suck.
# - Remove all references to old code which used hardcoded values.
# - Fix up the interface and arg checks to use argparse instead of sys calls.
# - Other misc cleanups.
#
#
# Enjoy!
# -SCRAMBLR
#
import sys
from scapy.all import *


if len(sys.argv) < 3:
    print("dude read the documentation. you need to run this with 2 variables:")
    print("server$ ./spooftest.py destinationserver 123numberofpackets")
    print("")
    print("Quitting and letting you think about what you've done!!!!!111")
    sys.exit()
else:
 howmany = 666                          # Change this..
 destination = "localhost"              # Change em via command line with this version..
 message = "HISEXYITSSPOOFTESTDOTPY"
 destx= sys.argv[1]
 numbs= sys.argv[2]                     # Initalizing both string and
 numbi= int(sys.argv[2])                # int values for use in diff places. im sure theres
                                        # a way better way to do this but i like writing
                                        # garbage to piss coders off lol.

# Please make sure to enjoy my use of mixed SPACES and TABS. I know u love it. lmfao

print("IP Spoofing / IPHM Test Tool")
print("IP Header Modification & Verification Tool")
print("Now With 100% LESS CAIDA!!")
print("")
print("Created by SCRAMBLR (https://github.com/scramblr)\r\n\r\n")
print("[*] We're gonna be spoofing now!")
print("[*] How many packjets r we sending? "+ numbs + "")
print("[*] Sending deez spiffy, spoofy pack3t boiz to: " +destx + "")
print("")
print("[*] Verifying " + destx + " still lives on the internet with ICMP ping...")
sr1(IP(dst=destx)/ICMP()/"SCRAMBLRALIVEPING", timeout=2)
print("")
print("-----------------------^^^^^^")
print("[*] Unless the above says GOT 0 ANSWERS, we're gonna execute in a sec.")
print("[*] ..even if it DOES say that, who cares.. maybe you're blocking ICMP.")
print("[*] CTRL+C To Abort if you're sure you fucked up...")
__import__("time").sleep(4)
print("[*] Sending some spoofy packjets to da box!")
packjet = IP(src=RandIP(),dst=destx)/ICMP()/message
send(packjet,count=numbi)

__import__("time").sleep(1)

print("[*] w00t! ok we sent " + numbs + " ICMP packjets to " + destx + " so hopefully you")
print("[*] were running tcpdump on that server to watch for the packets. otherwise, log in to the")
print("[*] destination server and run, as root, # tcpdump -i any -nnnv -c 5000 icmp <-- and then")
print("[*] re-run this script on the spoofy server again to send the blast of packets to the server")
print("")
print("[*] check https://github.com/scramblr/spooftest for updates!")
print("[*] © MMXXIV SCRAMBLR")
