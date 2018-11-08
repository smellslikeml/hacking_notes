#!/usr/bin/env python
from scapy.all import *

def pkt_callback(pkt):
    print(pkt.show())

if __name__ == '__main__':
    N = 10
    sniff(filter="",prn=pkt_callback,count=N)

