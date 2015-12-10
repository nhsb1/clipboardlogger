import pyperclip
import time
import datetime
import sys
import os
from sys import argv
from argparse import ArgumentParser

#Clipboard to Text File - saves clipboard items to an arbitrary text file, appending

parser = ArgumentParser(description = 'cxz - copy paste to text')
parser.add_argument("-f", "--file", dest="filename", help="file name to write output", metavar="FILE")
parser.add_argument("-s", "--save", action="store_true", dest="savetrue", default=False, help="save current string to clipboard")
parser.add_argument("-c", "--current", action="store_true", dest="clipboardnow", default=False, help="print current clipboard content")
parser.add_argument("-r", "--read", action="store_true", dest="readfile", default=False, help="print the content of the specified file")
args = parser.parse_args()

if args.clipboardnow:
	currentclipboard = pyperclip.paste()
	print currentclipboard

if args.savetrue:
	if args.filename:
		currentclipboard = pyperclip.paste()
		target = open(args.filename, "a")
		target.write(currentclipboard)
		target.write("\n")
		print currentclipboard
	else:
		print "Please specify an output file.  -f filename.txt"

if args.readfile:
	if args.filename:
		target = open(args.filename)
		print target.read()
	else:
		print "Please specify a file to read.  -f filename.txt"		

