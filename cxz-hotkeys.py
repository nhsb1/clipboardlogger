import pyhk
import sys
from argparse import ArgumentParser
import pyperclip
import datetime


#Clipboard to Text File - saves clipboard items to an arbitrary text file, appending
#Dependencies: pyhk, pyhook, pywin32, sys, argparse, pyperclip, datetime
#
#Dependency notes:
#pyHook, pyWin32 available here: http://www.lfd.uci.edu/~gohlke/pythonlibs/
#To install: pip install *.whl 
#Make sure to run: python.exe Scripts\pywin32_postinstall.py -install (from cmd launched as administrator)

parser = ArgumentParser(description = 'cxz - copy paste to text')
parser.add_argument("-f", "--file", dest="filename", help="file name to write output", metavar="FILE")
parser.add_argument("-s", "--save", action="store_true", dest="savetrue", default=False, help="save current string to clipboard")
args = parser.parse_args()

def blankfile():
	newnow = str(datetime.datetime.now().date()) + ".txt"
	print "No filename specified.  Next time, use (-f filename.txt), saving to: " + newnow
	print "Exit hotkey is: CTRL+ALT+0"
	print "To print contents of %r, CTRL+E." %newnow
	args.filename=newnow

def readfile():
	if args.filename:
		target = open(args.filename)
		fileread = target.read() #reads the contents of the file file
		pyperclip.copy(fileread) #copies the contents of the specified file to the clipboard
		print fileread

	else:
		print "Please specify a file to read.  -f filename.txt"	

def savepaste():
    if args.savetrue:
		currentclipboard = pyperclip.paste() #gets the contents of the clipboard 
		currentclipboard = currentclipboard.encode('utf-8') #cleans the string with utf-8 envoding
		currentclipboard = currentclipboard.strip() #strips the whitespaces
		target = open(args.filename, "a") #opens the specified file for appending
		target.write(currentclipboard)
		target.write("\n")
		#print currentclipboard
		print ">"

def terminate():
	sys.exit() 

#create pyhk class instance
hot = pyhk.pyhk()

#add hotkey
hot.addHotkey(['Alt', 'C'],savepaste)
hot.addHotkey(['Ctrl', 'Alt', '9'],blankfile)
hot.addHotkey(['Ctrl', 'E'],readfile)
hot.addHotkey(['Ctrl', 'Alt','0'],terminate)

if args.filename:
	print "Exit hotkey is: CTRL+ALT+0"
	print "To print contents of current file, CTRL+E."
	hot.start()
else:
	blankfile()
	hot.start()
