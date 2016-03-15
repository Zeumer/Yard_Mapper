# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import datetime
import magFunctions
import select
import struct
import time
import bluetooth._bluetooth as bluez

dev_id = [0, 1, 2]

test = []

numSockets = 2
#le = open('logfile', 'w')


#blescan.hci_le_set_scan_parameters(sock)
#blescan.hci_enable_le_scan(sock)

def printpacket(pkt):
    for c in pkt:
        sys.stdout.write("%02x " % struct.unpack("B",c)[0])
def createSocket(port_id):
	try:
		sock = bluez.hci_open_dev(port_id)

		print "ble thread started on ", port_id
			
		blescan.hci_le_set_scan_parameters(sock)
		blescan.hci_enable_le_scan(sock)
		old_filter = sock.getsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, 14)
		flt = bluez.hci_filter_new()
		bluez.hci_filter_all_events(flt)
		bluez.hci_filter_set_ptype(flt, bluez.HCI_EVENT_PKT)
                sock.setsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, flt )

	        test.append(sock)
	except:
		print "error accessing bluetooth device on ", port_id
#    		sys.exit(1)
def createAllSockets():
	for num in range(0,len(dev_id)):
		for i in range(0, numSockets):
			createSocket(num) 

def closeAllSockets():
	for num in range(0,len(test)):
		test[0].close()
	print "Before delete ",test
	del test[:]
	print "After delete ",test

createAllSockets()

while True:
	report_pkt_offset = 0

#	createAllSockets()
	
#	phread, phwrite, pherror = select.select(test, [], [], 60)
	ready_to_read, ready_to_write, in_error = select.select(test, [], [], 60)
	
#	while ready_to_read[i].recv(255) == 0:
 #                       print "In loop"


#	print len(ready_to_read)
	for i in range(0, len(ready_to_read)):
		
		pkt = ready_to_read[i].recv(255)
		
		ptype, event, plen = struct.unpack("BBB",  pkt[:3])
		print "-------------", ready_to_read[i].getsockname()
       		print "\tfullpacket: ", printpacket(pkt)
    		print datetime.datetime.now()

		print "\tUDID: ", printpacket(pkt[report_pkt_offset -22: report_pkt_offset - 6])
    		print "\tMAJOR: ", printpacket(pkt[report_pkt_offset -6: report_pkt_offset - 4])
    		print "\tMINOR: ", printpacket(pkt[report_pkt_offset -4: report_pkt_offset - 2])
#                print "\tMAC address: ", packed_bdaddr_to_string(pkt[report_pkt_offset + 3:report_pkt_offset + 9])
    		    	# commented out - don't know what this byte is.  It's NOT TXPower
                txpower, = struct.unpack("b", pkt[report_pkt_offset -2])
                print "\t(Unknown):", txpower

                rssi, = struct.unpack("b", pkt[report_pkt_offset -1])
                print "\tRSSI:", rssi

 #   	closeAllSockets()
 #   	time.sleep(.1)

