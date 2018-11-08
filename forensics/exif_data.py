#!/usr/bin/env python
from pprint import pprint
from subprocess import Popen, PIPE


def exif_data(img_pth):
    p = Popen('exiftool ' + img_pth, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    output, err = p.communicate()
    exif_data = output.decode('utf8').split('\n')
    pprint(exif_data)

if __name__ == '__main__':
    import sys
    img_pth = sys.argv[1]
    exif_data(img_pth)
