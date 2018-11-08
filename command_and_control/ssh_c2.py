#!/usr/bin/env python
'''
Simple SSH c2, load & parse hosts.csv
              IP,user,password
execute commands with sudo and print to STDOUT
'''
import sys
from pssh.clients import ParallelSSHClient

cmd = sys.argv[1]
host_lst = 'hosts.csv'

with open(host_lst, 'r') as infile:
    data = infile.readlines()
host_lst = [host.strip().split(',') for host in data]
host_config = {}
for host in host_lst:
    try:
        host_config[host[0]] = {'user': host[1], 'password': host[2]}
    except:
        pass
hosts = host_config.keys()
client = ParallelSSHClient(hosts, host_config=host_config)
output = client.run_command(cmd, sudo=True)

for host, host_output in output.items():
    for line in host_output.stdout:
        print(host, line)
