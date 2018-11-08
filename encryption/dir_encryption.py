#!/usr/bin/env python
import os
import fnmatch
from cryptography.fernet import Fernet
import sys

if len(sys.argv) != 3:
    print('Usage: python dir_encrypt.py <target_dir> <doc_type>')
    sys.exit(1)
else:
    target_dir = sys.argv[1]
    doc_type = sys.argv[2]

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
    for filename in fnmatch.filter(fl, '*%s' % doc_type):
        doc = os.path.join(rt, filename)
        with open(doc, 'rb') as infile:
            data = infile.read()
        token = f.encrypt(data)
        with open(doc + '.bin', 'w') as encrypted_file:
            encrypted_file.write(token.decode())
print('Done')
