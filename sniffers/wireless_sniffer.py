#!/usr/bin/env python
from scapy.all import *

sniff(iface="wlp2s0",prn=lambda x:x.sprintf("{Dot11Beacon:%Dot11.addr3%\t%Dot11Beacon.info%\t%PrismHeader.channel%\t%Dot11Beacon.cap%}"))
