#David Evans, Yard Mapper, March 8, 2016

import magFunctions
import time

magFunctions.init_magnetometer()#You must run this before running magnetometer

print magFunctions.read_bearing() 

time.sleep(1)

while(True):
	bearing = magFunctions.read_bearing() #get the magnetometer bearing

	print bearing

	time.sleep(1);#Take a rest
