import bluetoothFunctions
import packetFunctions

returnedlist = []

bluetoothFunctions.initBluetoothSearching()

returnedList = bluetoothFunctions.getBeacons();

returnedList = bluetoothFunctions.getBeacons();
returnedList = bluetoothFunctions.getBeacons();
while True:
	returnedList = bluetoothFunctions.getBeacons();

	for beacon in returnedList:
		print "_____"
		print packetFunctions.getUUID(beacon)
		print "_____"
#print returnedList
