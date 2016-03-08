import magFunctions
import time

magFunctions.init_magnetometer()

while(True):
	bearing = magFunctions.read_bearing()

	print bearing

	time.sleep(1);