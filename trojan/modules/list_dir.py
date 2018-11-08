#!/usr/bin/env python
import os

def run(**args):
    print('[*] In list_dir module.')
    files = os.listdir('.')
    return str(files)
