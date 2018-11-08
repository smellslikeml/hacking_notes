#!/usr/bin/env python
import sys
from scapy.all import *

target=sys.argv[1]
send( fragment(IP(dst=target)/ICMP()/("X"*60000)) ) # dst="10.0.0.5"
