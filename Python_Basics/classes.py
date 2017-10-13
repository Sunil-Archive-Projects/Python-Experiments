#defining classes 
class myClass():
	def firstMethod(self):
		#self refers to itself
		print("First Method")

	def secondMethod(self,str):
		#self refers to itself
		print "Second Method",str

#defining subclasses
#	subClass inherits superClass myClass

class subClass(myClass):
	x=0



def main():
	obj=subClass()
	obj.firstMethod()
	obj.secondMethod("Arg1")

main()


