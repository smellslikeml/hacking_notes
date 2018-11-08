#!/usr/bin/env python
'''
Extract exif data from jpeg files.
[Usage]
   python pil_exif.py /path/to/file.jpg
'''
from PIL import Image, ExifTags

def pil_exif(img_pth):
    img = Image.open(img_pth)
    print({ ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS })


if __name__ == '__main__':
    import sys
    img_pth = sys.argv[1]
    pil_exif(img_pth)
