#!/usr/bin/env python
'''
https://arxiv.org/pdf/1810.10109.pdf
'''
from scapy.all import *

def prnRSSI(pkt):
    #print(pkt[RadioTap].dBm_AntSignal)
    #if (pkt[RadioTap].addr1 or pkt[RadioTap].add2) == '2c:30:33:d1:bc:49':
    try:
        print(pkt[RadioTap].info, pkt[RadioTap].addr1, pkt[RadioTap].addr2, pkt[RadioTap].addr3, -(256-ord(pkt[RadioTap].notdecoded[-4:-3])))
    except:
        print(pkt[RadioTap].addr1, pkt[RadioTap].addr2, pkt[RadioTap].addr3, -(256-ord(pkt[RadioTap].notdecoded[-4:-3])))

sniff(iface='wlp2s0mon', prn=prnRSSI)



