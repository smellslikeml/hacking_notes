#!/usr/bin/env python
import sys
from bluetooth import *

def sdpBrowse(addr):
    services = find_service(address=addr)
    for service in services:
        name = service['name']
        proto = service['protocol']
        port = str(service['port'])
        print('[+] Found ' + str(name) + ' on ' + str(proto) + ':' + port)

bt_addr = sys.argv[1]
sdpBrowse(bt_addr)
