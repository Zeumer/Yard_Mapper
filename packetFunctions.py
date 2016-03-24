#Goal of this class is to provide functions for the manipulation of packets
#e.g. reading UUID, Major, minor, transmit power
import struct

#readUUID
def getUUID(stringPkt):
	return stringPkt[0:31]
#readMajor
def readMajor(pkt):
#	return unpackAsString(pkt[report_pkt_offset -6: report_pkt_offset - 4])

#readMinor
def readMinor(pkt):
	#return unpackAsString(pkt[report_pkt_offset -4: report_pkt_offset - 2])

#readMACAddress
def readMACAddress(pkt):
	return unpackAsString(pkt[report_pkt_offset + 3:report_pkt_offset + 9])

#readTXPower
def readMajor(pkt):
#	return unpackAsString(pkt[report_pkt_offset + 3:report_pkt_offset + 9])

#readRSSI

#pktToString
def pktToString(pkt):
	report_pkt_offset = 0
	Adstring = returnstringpacket(pkt[report_pkt_offset -22: report_pkt_offset - 6]) 
    Adstring += ","
    Adstring += "%i" % returnnumberpacket(pkt[report_pkt_offset -6: report_pkt_offset - 4]) 
    Adstring += ","
    Adstring += "%i" % returnnumberpacket(pkt[report_pkt_offset -4: report_pkt_offset - 2]) 
    Adstring += ","
    Adstring += "%i" % struct.unpack("b", pkt[report_pkt_offset -2])
    Adstring += ","
    Adstring += "%i" % struct.unpack("b", pkt[report_pkt_offset -1])

    return Adstring

#unpackAsString
def returnstringpacket(pkt):
    myString = "";
    for c in pkt:
        myString +=  "%02x" %struct.unpack("B",c)[0]
    return myString 

def returnnumberpacket(pkt):
	myInteger = 0
	multiple = 256
	for c in pkt:
	    myInteger +=  struct.unpack("B",c)[0] * multiple
	    multiple = 1
	return myInteger 