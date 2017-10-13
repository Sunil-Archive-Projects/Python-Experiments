import os
import sys

files = os.listdir()
path="C:\Temp\Software\\ffmpeg_64bit\\bin\\ffmpeg -i"
config="-vn -ar 48000 -ab 192000 -ac 2"

for file in files:
	if(file.endswith(".mp4")):
		audioFile=file.replace(".mp4", ".mp3")
		cmd=path+" \""+file+"\" "+config+" \""+audioFile+"\""
		print(cmd)
		os.system(cmd)