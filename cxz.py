import pyhk
import sys 
import os
from argparse import ArgumentParser
import pyperclip
import datetime

#.26
#Clipboard to Text File - saves clipboard items to an arbitrary text file, appending
#Dependencies: pyhk, pyhook, pywin32, sys, argparse, pyperclip, datetime
#
#Dependency notes:
#pyHook, pyWin32 available here: http://www.lfd.uci.edu/~gohlke/pythonlibs/
#To install: pip install *.whl 
#Make sure to run: python.exe Scripts\pywin32_postinstall.py -install (from cmd launched as administrator)
#Feature request:
#1. timestamp on content changes
#2. Clear all (?) clipboard lists
#3. Get most recent item out of list and back to clipboard?
#4. Add E and R to clipboard lists; add O and P to clipboard DIR list
#5. Load hotkeys from config file - user editable?

cliplistq = []
cliplistw=[]
clipliste=[]
cliplistr=[]
newnow = ""

parser = ArgumentParser(description = 'cxz - copy paste to text')
parser.add_argument("-f", "--file", dest="filename", help="file name to write output", metavar="FILE")
parser.add_argument("-s", "--save", action="store_true", dest="savetrue", default=False, help="save current string to clipboard")
args = parser.parse_args()

def blankfile():
	global newnow
	newnow = str(datetime.datetime.now().date()) + ".txt"
	print "-------------------------------------------------------------------------------"
	print "No filename specified.  Next time, use (-f filename.txt), saving to: " + newnow
	print "Active Clipboards - hotkey: CTRL+ALT+Q,W,E,R"
	print "List Clipboard content - hotkey: CTRL+ALT+U,I,O,P"
	print "Save all lists to current file - hotkey: CTRL+ALT+S"
	print "Load/Print active save file to console - hotkey: CTRL+ALT+L"
	print "Show help: CTRL+ALT+H"
	print "-------------------------------------------------------------------------------"
	args.filename=newnow

def readfile():
	if args.filename:
		target = open(args.filename)
		fileread = target.read() #reads the contents of the file file
		pyperclip.copy(fileread) #copies the contents of the specified file to the clipboard
		print fileread

	else:
		print "Please specify a file to read.  -f filename.txt"	

def mylistq(): #add current clipboiard to my temporary list
	tmpclip = ""
	tmpclip = pyperclip.paste()
	tmpclip = tmpclip.encode('utf-8')
	tmpclip = tmpclip.strip()
	global cliplistq
	cliplistq.append(tmpclip)
	print "Clipboard content added to templistQ>"


def qlistcontent():
	#print ">>"
	global cliplistq
	for i in cliplistq:
		print i

def mylistw(): #add current clipboiard to my temporary list
	tmpclip = ""
	tmpclip = pyperclip.paste()
	tmpclip = tmpclip.encode('utf-8')
	tmpclip = tmpclip.strip()
	global cliplistw
	cliplistw.append(tmpclip)
	print "Clipboard content added to templistW>"
	#global cliplist1
	#for i in cliplist1:
	#	print i

def wlistcontent():
	global cliplistw
	for i in cliplistw:
		print i


def myliste(): #add current clipboiard to my temporary list
	tmpclip = ""
	tmpclip = pyperclip.paste()
	tmpclip = tmpclip.encode('utf-8')
	tmpclip = tmpclip.strip()
	global clipliste
	clipliste.append(tmpclip)
	print "Clipboard  added to templistE>"


def olistcontent():
	#print ">>"
	global clipliste
	for i in clipliste:
		print i


def mylistr(): #add current clipboiard to my temporary list
	tmpclip = ""
	tmpclip = pyperclip.paste()
	tmpclip = tmpclip.encode('utf-8')
	tmpclip = tmpclip.strip()
	global cliplistr
	cliplistr.append(tmpclip)
	print "Clipboard  added to templistE>"


def plistcontent():
	#print ">>"
	global cliplistr
	for i in cliplistr:
		print i
	
def savefile():
	global cliplistq
	for i in cliplistq:
		#i = pyperclip.copy(i)
		#print i
		#print i
		currentclipboard = i
		target = open(args.filename, "a") #opens the specified file for appending
		target.write(currentclipboard)
		target.write("\n")
	global cliplistw
	for i in cliplistw:
		currentclipboard = i
		target = open(args.filename, "a") #opens the file for appending
		target.write(currentclipboard)
		target.write("\n")
	global clipliste
	for i in clipliste:
		currentclipboard = i
		target = open(args.filename, "a") #opens the file for appending
		target.write(currentclipboard)
		target.write("\n")
	global cliplistr
	for i in cliplistr:
		currentclipboard = i
		target = open(args.filename, "a") #opens the file for appending
		target.write(currentclipboard)
		target.write("\n")	
	print "Temporary Lists Committed to savefile>"
	#global cliplistq, cliplistw
	cliplistq=[]
	cliplistw=[]
	clipliste=[]
	cliplistr=[]



def savepaste(): #
    if args.savetrue:
		currentclipboard = pyperclip.paste() #gets the contents of the clipboard 
		currentclipboard = currentclipboard.encode('utf-8') #cleans the string with utf-8 envoding
		currentclipboard = currentclipboard.strip() #strips the whitespaces
		target = open(args.filename, "a") #opens the specified file for appending
		target.write(currentclipboard)
		target.write("\n")
		#print currentclipboard
		print "Clipboard content committed to savefile>"

def terminate():
	print "Save To: %r" %newnow
	#sys.exit(1) 
	os._exit(1)

#create pyhk class instance
hot = pyhk.pyhk()

#add hotkey
hot.addHotkey(['Ctrl', 'Alt', 'S'],savepaste)
hot.addHotkey(['Ctrl', 'Alt', 'H'],blankfile)
hot.addHotkey(['Ctrl', 'Alt', 'L'],readfile)
hot.addHotkey(['Ctrl', 'Alt', 'S'],savefile)
hot.addHotkey(['Ctrl', 'Alt', '0'],terminate)
hot.addHotkey(['Ctrl', 'Alt', 'Q'],mylistq)
hot.addHotkey(['Ctrl', 'Alt', 'U'],qlistcontent) 
hot.addHotkey(['Ctrl', 'Alt', 'W'],mylistw)
hot.addHotkey(['Ctrl', 'Alt', 'I'],wlistcontent) 
hot.addHotkey(['Ctrl', 'Alt', 'E'],myliste)
hot.addHotkey(['Ctrl', 'Alt', 'O'],olistcontent) 
hot.addHotkey(['Ctrl', 'Alt', 'R'],mylistr)
hot.addHotkey(['Ctrl', 'Alt', 'P'],plistcontent) 


if args.filename:
	print "Exit hotkey is: CTRL+ALT+0"
	print "To print contents of current file, CTRL+E."
	hot.start()
else:
	blankfile()
	hot.start()
