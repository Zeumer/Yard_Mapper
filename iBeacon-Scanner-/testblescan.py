# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import datetime

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

while True:
	returnedList = blescan.parse_events(sock, 1)
	print "----------"
#	print returnedList[0];
	for beacon in returnedList:
		print datetime.datetime.now()
#		t = type(beacon)
#		file.write(beacon)
#		file.write('\n')		
		print beacon

