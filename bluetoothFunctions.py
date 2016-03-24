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

socketList = []
beaconList = []

socketsPerPort = 2
#le = open('logfile', 'w')


#blescan.hci_le_set_scan_parameters(sock)
#blescan.hci_enable_le_scan(sock)


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

	        socketList.append(sock)
	except:
		print "error accessing bluetooth device on ", port_id
#    		sys.exit(1)
def createAllSockets():
	for num in range(0,len(dev_id)):
		for i in range(0, socketsPerPort):
			createSocket(num) 

def closeAllSockets():
	for num in range(0,len(socketList)):
		socketList[num].close()
	print "Before delete ",socketList
	del socketList[:]
	print "After delete ",socketList

def inBeaconList(beaconList, beacon):
	beaconUUID = getUUID(beacon)
	for i in range(0, len(beaconList):
		if beaconUUID == beaconList[i].getUUID()
			return True;
	return False

def initBluetoothSearching():
	createAllSockets()
	for i in range(0, len(dev_id))
		beaconList.append([])


def getBeacons():


#	createAllSockets()
	
#	phread, phwrite, pherror = select.select(test, [], [], 60)
	ready_to_read, ready_to_write, in_error = select.select(test, [], [], 60)
	
#	while ready_to_read[i].recv(255) == 0:
 #                       print "In loop"


#	print len(ready_to_read)
	for i in range(0, len(ready_to_read)):
		port = ready_to_read[i].getsockname()
		pkt = ready_to_read[i].recv(255)
	
		beacon = pktToString(pkt)
		
		if inBeaconList(beaconList[port], beacon) == False
			beaconList[port].append(beacon)

	return beaconList


 #   	closeAllSockets()
 #   	time.sleep(.1)

