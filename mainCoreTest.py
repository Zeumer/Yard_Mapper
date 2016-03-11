# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import datetime
import magFunctions
import select
import struct


import bluetooth._bluetooth as bluez

dev_id = 0

test = []
potwriter = []
errors = []
#file = open('logfile', 'w')
for i in range(0, 5):
	try:
		sock = bluez.hci_open_dev(dev_id)
		print "ble thread started"
		
		blescan.hci_le_set_scan_parameters(sock)
		blescan.hci_enable_le_scan(sock)
		
		


		old_filter = sock.getsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, 14)

		print "1"

		flt = bluez.hci_filter_new()
   		bluez.hci_filter_all_events(flt)
    		bluez.hci_filter_set_ptype(flt, bluez.HCI_EVENT_PKT)
    		sock.setsockopt( bluez.SOL_HCI, bluez.HCI_FILTER, flt )
		blescan.hci_le_set_scan_parameters
       		test.append(sock)
	except:
		print "error accessing bluetooth device..."
    		sys.exit(1)

#blescan.hci_le_set_scan_parameters(sock)
#blescan.hci_enable_le_scan(sock)

def printpacket(pkt):
    for c in pkt:
        sys.stdout.write("%02x " % struct.unpack("B",c)[0])

while True:
	report_pkt_offset = 0

	ready_to_read, ready_to_write, in_error = select.select(test, potwriter, errors, 60)

	print len(ready_to_read)
	for i in range(0, len(ready_to_read)):
		
		pkt =  ready_to_read[i].recv(255)	
		ptype, event, plen = struct.unpack("BBB",  ready_to_read[i].recv(255)[:3])
		print "-------------"
                print i        	#print "\tfullpacket: ", printpacket(pkt)
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

