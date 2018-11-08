#!/usr/bin/env python
import os
import fnmatch
from cryptography.fernet import Fernet
import sys

if len(sys.argv) != 2:
    print('Usage: python dir_decrypt.py <target_dir>')
    sys.exit(1)
else:
    target_dir = sys.argv[1]

if os.path.exists('f_key.txt'):
    with open('f_key.txt', 'r') as infile:
        key = infile.readline()
    key = key.strip().encode()
else:
    key = Fernet.generate_key()
    with open('f_key.txt', 'w') as outfile:
        outfile.write(key.decode() + '\n')

f = Fernet(key)
for rt, dr, fl in os.walk(target_dir):
    for filename in fnmatch.filter(fl, '*.bin'):
        if 'f_key' not in filename:
            doc = os.path.join(rt, filename)
            with open(doc, 'rb') as infile:
                data = infile.read()
            try:
                msg = f.decrypt(data)
                print(msg)
            except:
                print('--------- Error decrypting: %s ------------' % filename)
