#!/usr/bin/env python
import sys
from bluetooth import *

def rfcommCon(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((addr, port))
        print('[+] RFCOMM Port ' + str(port) + ' open')
        sock.close()
    except Exception as e:
        print('[-] RFCOMM Port ' + str(port) + ' closed')

bt_addr = sys.argv[1]
for port in range(1, 30):
    rfcommCon(bt_addr, port)
