#!/usr/bin/env python
'''
From: https://github.com/beatsbears/steg
hide_steg function succeeds with new.<extension>
in the current directory 
extract_steg function succeeds with hidden_file.<extension>
'''
from steg import steg_img

def hide_steg(img_pth, msg_pth):
    s = steg_img.IMG(payload_path=msg_pth, image_path=img_pth)
    s.hide()
    return

def extract_steg(img_pth):
    s = steg_img.IMG(image_path=img_pth)
    s.extract()
    return

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        img_pth = sys.argv[1]
        msg_pth = sys.argv[2]
        hide_steg(img_pth, msg_pth)
    elif len(sys.argv) == 2:
        img_pth = sys.argv[1]
        extract_steg(img_pth)
    else:
        print('Usage: \tpython steganography.py <img_pth> <mgs_pth> to encrypt to new.<extension>,\n\tpython steganography.py <img_pth> to decrypt message to hidden_file.<extension>')
        sys.exit(1)
