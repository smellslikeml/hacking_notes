#!/usr/bin/env python
'''
Logs cursor movement
Can be used to help determine if 
attacker is in a sandbox.
Use to develop ML model to identify
abnormal usage patterns for
intrusion detection.
'''
import os
import time
from Xlib import display

old_x = 0
old_y = 0
old_dur = 0
end_time = 0
logfile = os.environ['HOME'] + '/.cursor.log'

while True:
    data = display.Display().screen().root.query_pointer()._data
    new_x = data["root_x"]
    new_y = data["root_y"]
    if old_x != new_x or old_y != new_y:
        start_time = time.time()
        dur = start_time - end_time
        if dur > old_dur:
            pass
            with open(logfile, 'a') as outfile:
                outfile.write(':'.join(map(str, [new_x,new_y])) + ',')
        else:
            with open(logfile, 'a') as outfile:
                outfile.write('\n')
    else:
        end_time = time.time()
    old_x = new_x
    old_y = new_y
    old_dur = dur
