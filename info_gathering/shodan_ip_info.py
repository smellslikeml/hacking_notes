#!/usr/bin/env python
'''
[Documentation]
    https://shodan.readthedocs.io/en/latest/

[Installation]
    pip install shodan

[Basic Usage]
    import shodan

    SHODAN_API_KEY = 'your key here'
    api = shodan.Shodan(SHODAN_API_KEY)
'''
import os
import re
import sys
import shodan

try:
    SHODAN_API_KEY = os.environ['SHODAN_API_KEY']
except:
    print('export Shodan API key in ~/.bashrc')
    sys.exit(1)

api = shodan.Shodan(SHODAN_API_KEY)

def target_info(target):
    target = str(target)
    is_ip = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", target)
    if is_ip:
        host = api.host(target)

        print("""
                IP: {}
                Organization: {}
                Operating System: {}
        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        try:
            for item in host['vulns']:
                CVE = item.replace('!','')
                print('Vulns: %s' % item)
                exploits = api.exploits.search(CVE)
                for item in exploits['matches']:
                    if item.get('cve')[0] == CVE:
                        print(item.get('description'))
        except:
            pass

        for item in host['data']:
            print("""
                    Port: {}
                    Banner: {}
            """.format(item['port'], item['data']))
    else:
        for tgt in target:
            is_hostname = re.match("^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$", tgt)
            if is_hostname:
                query = ' '.join(target)
                result = api.search(query)

                for service in result['matches']:
                    print(service['ip_str'])

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python shodan_ip_info.py <target IP>')
        sys.exit(1)
    if len(sys.argv) == 2:
        TARGET = sys.argv[1]
    elif len(sys.argv) > 2:
        TARGET = sys.argv[1:]
    target_info(TARGET)
