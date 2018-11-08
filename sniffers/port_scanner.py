#!/usr/bin/env python
import sys
from scapy.all import *

target_ip=sys.argv[1]
res, unans = sr( IP(dst=target_ip)/TCP(flags="S", dport=(1,1024)) )

print(res)
