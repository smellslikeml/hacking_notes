#!/usr/bin/env python
from scapy.all import *

ans, unans = srloop(IP(dst="192.168.1.1")/TCP(dport=80,flags="S"))


