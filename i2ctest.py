import smbus
import time
bus = smbus.SMBus(1)
address = 0x1e


bus.write_byte_data(address, 2, 0x00)

def read_word
while True:
       # bearing = bearing3599()     #this returns the value to 1 decimal place in degrees. 
       # bear255 = bearing255()      #this returns the value as a byte between 0 and 255. 
       # print bearing
       # print bear255
	print "reading:"
	print "x:"       
	print bus.read_byte_data(address, 3)
	print bus.read_byte_data(address, 4)
	print "z:"
	print bus.read_byte_data(address, 5)
	print bus.read_byte_data(address, 6)
	print "y:"
	print bus.read_byte_data(address, 7)
	print bus.read_byte_data(address, 8)

	time.sleep(5)
