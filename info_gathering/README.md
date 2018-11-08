# Gathering Information

Attackers collect information on potential targets to help find vulnerabilities. Most computers come with the Python programming language by default. This makes python great for building custom tools. 

Some tools for information gathering include APIs like:

* Twitter, Facebook, Google+ (social media)
* Shodan (vulnerability search engine)

or techniques in:

* Google Dorking/Hacking (advanced search)
* web scraping

which can be brought together with python client libraries like Tweepy, Shodan, Scrapy or the standard request library.

## Usage

Try the cheat sheet in google_dorking.md for manual info gathering through the browser, for example try the search query:
```
query terms filetype:xls
```

Hackers may use Google Dorking to find sensitive files on misconfigured servers to turn up email contacts for a phishing campaign. While password lists may be augmented by tokenizing the text content of a target domain.

Shodan offers a search engine of service banners for internet connected devices. To search vulnerabilities using Shodan, obtain an API key and set the SHODAN_API_KEY environment variable, then run:
```
python shodan_ip_info.py <target_url_or_ip>
```

OSINT APIs and Google Hacking are **passive discovery** methods. These methods may produce useful information without touching a target host. 

To contrast, **active discovery** methods like web spidering or port scanning may turn up additional information at the risk of triggering a network intrusion detection system.

To limit the information provided to the target host, you might prefer to use proxies. To start a tor proxy, run:
```
sudo apt-get install tor
```
Now you can use the default tor proxy port 9050 with requests. Verify with:
```
import requests

local_proxy = 'socks5://localhost:9050'
socks_proxy = {
    'http': local_proxy,
    'https': local_proxy
}

current_ip = requests.get(
    url='http://icanhazip.com/',
    proxies=socks_proxy,
    verify=False
)
print(current_ip.text)
```

Scrapy provides a powerful web data extraction framework. We introduce the proxy server polipo to help Scrapy use the SOCK5 protocol to crawl anonymously with Tor. To install these tools:
```
pip install scrapy
sudo apt-get install polipo
```
From the scrapy docs, to create a new Scrapy project, use:
```
scrapy startproject <project_name>
```
Add the following to the settings.py file in your new project to use proxy middleware: 
```
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]
HTTP_PROXY = 'http://127.0.0.1:8123'
DOWNLOADER_MIDDLEWARES = {
     'project_name.middlewares.RandomUserAgentMiddleware': 400,
     'project_name.middlewares.ProxyMiddleware': 410,
     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None
}
```
Finally we create the middlewares.py file:
```
import os
import random
from scrapy.conf import settings

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')
```
Add this file to the same directory as your settings.py file in the scrapy project. Now you will be able to spider target urls over tor and extract elements with xpath.

Recon-ng comes well-recommended for a more fully developed open source reconnaissance package.
Tools like slurp (depends on Go) offer S3 bucket enumeration for a target domain with the command:
```
./slurp domain --domain <target_domain>
```

For port scanning, nmap and it's python wrapper python-nmap are useful open source tools. For example, nmap -sP target_ip can be called like:
```
import nmap
nm = nmap.PortScanner()
scan_results = nm.scan(<target_ip>, <target_ports>, arguments='sP')
```

If these tools are not available on your host, you may write a port scanner using python sockets library.

Often, a manual inspection of screenshots taken of HTTP(s) services will help to filter out pages unlikely to provide useful information. This can be automated with the use of a tool like EyeWitness or by building a web page rendering tool with PyQt5.

To screenshot a web page, install PyQt5 and run:
```
python pyqt5_screenshot.py <target_url>
```

