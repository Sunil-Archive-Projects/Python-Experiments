x=100

#while loop
while(x>0):
	#print x
	x=x-1

#for loop
for x in range(5,10):
	if x==9:
		break

	print x

#collection iteration
days=["w","t","f"]
for d in days:
	print d

#printing with index as well
for i,d in enumerate(days):
	print i,d
	