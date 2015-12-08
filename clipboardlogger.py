import pyperclip
import time
import datetime
import sys
import os
from sys import argv

script, filename = argv
target = open(filename, 'w')

init_value = ""
print "Initalizing clipboard with null value... "
print "(Paste events echo'd to console, overwriting %r; CTRL-C to exit)" %filename
newnow = datetime.datetime.now()
pyperclip.copy("")

while True:
    i = input("")
    current_paste = pyperclip.paste()
    if current_paste != init_value:
        init_value = current_paste
        print "Clipboard Changed: %s" % str(current_paste)[:1000]
        target.write(current_paste)
        target.write("\n")
    time.sleep(0.1)
