#!/usr/bin/env python
'''
https://arxiv.org/pdf/1810.10109.pdf
#print(pkt[RadioTap].dBm_AntSignal)
'''
from scapy.all import *

def prnRSSI(pkt):
    try:
        print(pkt[RadioTap].info, pkt[RadioTap].addr1, pkt[RadioTap].addr2, pkt[RadioTap].addr3, -(256-ord(pkt[RadioTap].notdecoded[-4:-3])))
    except:
        print(pkt[RadioTap].addr1, pkt[RadioTap].addr2, pkt[RadioTap].addr3, -(256-ord(pkt[RadioTap].notdecoded[-4:-3])))

sniff(iface='wlp2s0mon', prn=prnRSSI)



