#python3
def main():
	f = open("testTxt.txt","a+")

	for i in range(0,10):
		f.write("Yo %d \r" % i)

	f.close()

	f=open("testTxt.txt","r")


	print f.read()
	print f.mode

	fl=f.readlines()
	for x in fl:
		print x



main()
