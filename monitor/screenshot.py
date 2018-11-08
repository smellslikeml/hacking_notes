#!/usr/bin/env python
import os
import subprocess
from Xlib import display, X
from PIL import Image 


cmd = ['xrandr']
cmd2 = ['grep', '*']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
p.stdout.close()
 
resolution_string, junk = p2.communicate()
resolution = resolution_string.split()[0].decode("utf-8") 
W, H = map(int, resolution.split('x'))

dsp = display.Display()
root = dsp.screen().root
raw = root.get_image(0, 0, W,H, X.ZPixmap, 0xffffffff)
image = Image.frombytes("RGB", (W, H), raw.data, "raw", "BGRX")
file_path = os.path.join(os.environ['HOME'], '.screenshot.png')
image.save(file_path)
