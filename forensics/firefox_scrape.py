#!/usr/bin/env python
import re
import sqlite3

def printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
    print('\n[*] --- Files Downloaded --- ')
    for row in c:
        print('[+] File: ' + str(row[0]) + ' from source: ' + str(row[1]) + ' at: ' + str(row[2]))

def printCookies(cookiesDB):
    try:
	conn = sqlite3.connect(cookiesDB)
	c = conn.cursor()
	c.execute('SELECT host, name, value FROM moz_cookies')
	print('\n[*] -- Found Cookies --')
	for row in c:
	    host = str(row[0])
	    name = str(row[1])
	    value = str(row[2])
	    print('[+] Host: ' + host + ', Cookie: ' + name + ', Value: ' + value)
    except Exception, e:
	if 'encrypted' in str(e):
	    print('\n[*] Error reading your cookies database.')
	    print('[*] Upgrade your Python-Sqlite3 Library')

def printHistory(placesDB):
    try:
	conn = sqlite3.connect(placesDB)
	c = conn.cursor()
	c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	print('\n[*] -- Found History --')
	for row in c:
	    url = str(row[0])
	    date = str(row[1])
            print('[+] ' + date + ' - Visited: ' + url)
    except Exception, e:
        if 'encrypted' in str(e):
            print('\n[*] Error reading your places database.')
            print('[*] Upgrade your Python-Sqlite3 Library')
            exit(0)

def printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    print('\n[*] -- Found Google --')
    for row in c:
        url = str(row[0])
        date = str(row[1])
        if 'google' in url.lower():
            r = re.findall(r'q=.*\&', url)
            if r:
                search=r[0].split('&')[0]
                search=search.replace('q=', '').replace('+', ' ')
                print('[+] '+date+' - Searched For: ' + search)

if __name__ == "__main__":
    import sys
    downloadDB = sys.argv[1]
    printDownloads(downloadDB)
