#normal function
def normal():
	print('Normal')

#function with arguments
def arguments(one,two):
	print('With arguments')

#function with return value
def returnVal(one,two):
	print('With Return')
	return one+two

#function with variable number of arguments
def variableArgs(*args):
	for x in args:
		print x
	return x

print variableArgs(1,2,3)