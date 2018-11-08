#!/usr/bin/env python
from scapy.all import *
ap_lst = []
def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap_lst:
                ap_lst.append(pkt.addr2)
                print('AP MAC: %s with SSID: %s' %(pkt.addr2, pkt.info))

sniff(iface='wlp2s0mon', prn=PacketHandler)
