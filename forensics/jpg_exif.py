#!/usr/bin/env python
'''
Extract exif data from jpeg files.
[Usage]
   python jpg_exif.py /path/to/file.jpg
'''
from PIL import Image, ExifTags

def jpg_exif(img_pth):
    img = Image.open(img_pth)
    print({ ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS })


if __name__ == '__main__':
    import sys
    img_pth = sys.argv[1]
    jpg_exif(img_pth)
