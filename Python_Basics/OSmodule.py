#!python3
import os
from os import path
#import datetime
import time

def main():
	print os.name

	print "Item Exists :",str(path.exists("testTxt.txt"))
	print "Is File? :",str(path.isfile("testTxt.txt"))
	print "Is Directory? :",str(path.isdir("/"))

	print "Items path :",str(path.realpath("testTxt.txt"))
	print "Items path and name :",str(path.split(path.realpath("testTxt.txt")))

	print "Last Modified at :",time.ctime(path.getmtime("testTxt.txt"))

main()