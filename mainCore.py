# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import datetime
import magFunctions
import time
import bluetooth._bluetooth as bluez

dev_id = 0

#file = open('logfile', 'w')

try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

magFunctions.init_magnetometer()

while True:
	print "------------------"
	print datetime.datetime.now()
	returnedList = blescan.parse_events(sock, 5)
#	print "----------" + datetime.datetime.now()
	print datetime.datetime.now()
	print magFunctions.read_bearing()
#	print datetime.datetime.now()
#	print returnedList[0];

	for beacon in returnedList:
		print datetime.datetime.now()
#		print magFunctions.read_bearing()
#		t = type(beacon)
#		file.write(beacon)
#		file.write('\n')		
		print beacon
#		time.sleep(1)
        sock.close()
        break
