from easygui import *
import sys
import pyperclip
from argparse import ArgumentParser

parser = ArgumentParser(description = 'cxz - copy paste to text')
parser.add_argument("-f", "--file", required=True, dest="filename", help="file name to write output", metavar="FILE")
args = parser.parse_args()

while 1:

    msg = "Clipboard Assistant"
    title = "Clipboard Assistant v1.0"
    choices=['Clipboard','Save','Quit']
    choice=buttonbox(msg, title,choices)
    if choice=='Clipboard':
        currentclipboard = pyperclip.paste()
        currentclipboard = currentclipboard.encode('utf-8') #cleans the string with utf-8 envoding
        currentclipboard = currentclipboard.strip() #strips the whitespaces
        codebox("Contents of Clipboard", "Contents:", currentclipboard)
        # fdsaf
    elif choice=='Save':
        target = open(args.filename, "a")
        target.write(currentclipboard)
        target.write("\n")
        msgbox("Clipboard content saved to file")

    elif choice=='Quit':
        sys.exit(0)
