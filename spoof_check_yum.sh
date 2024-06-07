#!/bin/bash
# SPOOF_CHECK TOOL
# released June 7 2024 by SCRAMBLR
# v0.11a
# https://github.com/scramblr/spooftest

echo ''
echo 'spoof_check_apt.sh for APTITUDE based *NIX Servers like Ubuntu, Debian, Etc. Run spoof_check_yum.sh for YUM based distros.'
echo ''
echo 'This tool will download the prerequisits and then ask for the server you have tcpdump running on before launching a small test that will prove whether the server is in fact spoofing packets.'
echo 'spoof_check.py does NOT USE CAIDA Spoof Tools or any other tools like it, because we are not dumb. Anyone who uses tools like that are BEGGING for their providers to be shut down.'
echo ''
echo 'Installing scapy and a few other tools...'
echo 'This may take up to 5 minutes.'
echo 'Pausing for 5 seconds in case you want to bail. 5...4...'
sleep 5
apt-get update
apt-get install net-tools bind-utils tcpdump python3-pip -y;pip install scapy
echo 'Tool installation complete.'
echo ''
echo ''
echo 'Next, Launch the included spooftest.py that comes with the repo github.com/scramblr/spooftest.git'
echo 'server$ python3 spooftest.py 1.2.3.4 100'
echo 'USAGE: spooftest.py <dest server> <# of packets>'
echo
