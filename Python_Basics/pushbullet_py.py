from pushbullet import Pushbullet

pushbullet_auth_filepath="C:\Temp\Python_auth\pusbullet_authkey.txt"

with open(pushbullet_auth_filepath) as f:
	authkey=f.readline()
	pb = Pushbullet(authkey.strip())
	push = pb.push_note("Python Notification Head", "Python Body")

	print(pb.devices)