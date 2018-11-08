#!/usr/bin/env python
'''
[Usage]
    sudo python network_sniffer.py
'''
from scapy.all import *

pkts = sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
