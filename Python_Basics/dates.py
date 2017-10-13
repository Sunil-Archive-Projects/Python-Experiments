#A date with python

from datetime import date
from datetime import time
from datetime import datetime

def main():
	today=date.today()
	print "Today is",today
	print "Day",today.day
	print "Month",today.month
	print "Year",today.year
	#weekday starts from 0 to 6
	print "Weekday :",today.weekday()

	#getting date and time
	
	print "DateTime",datetime.now()
	#getting time
	print "Time", datetime.time(datetime.now())

main()
