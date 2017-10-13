#!python3
import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
	if path.exists("testTxt.txt"):
		#make a backup  in .bak format
		src=path.realpath("testTxt.txt")

		head,tail=path.split(src)

		dst=src+".bac"

		#simple copy
		shutil.copy(src,dst)
		print "copied"

		#deep copy with stats
		#shutil.copystat(src,dst)

		#rename
		#os.rename("testTxt.txt","demoText.txt")

		#create zip file
		root_dir,tailx=path.split(src)
		#archive-filename zip-format 
		shutil.make_archive("python_learnings","zip",root_dir)
		print "ARchived!!"

		#finer control over the zipping process with ZipFile module

		newzip=ZipFile("zipfile.zip","w")
		newzip.write("testTxt.txt")

main()