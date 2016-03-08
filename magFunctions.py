#!/usr/bin/python
import smbus
import time
import math

bus #bus for i2c
address #address for device

#read_byte############################################################
#reads contents in a register
#Param: address of the target register
#Return: 4 bits of the contents in the register
def read_byte(adr):
    return bus.read_byte_data(address, adr)

#read_word############################################################
#reads combination of 2 registers
#   register 1 is MSB(Most significant byte)
#   register 2 is LSB(Least significant byte)
#Param: address of first target register
#Return: Returns 8 bits of contents in register 1 and register 2
def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

#read_word_2c############################################################
#reads combination of 2 registers, and converts the output to two's complement
#Param: address of first target register
#Return: Combination of contents of register 1 and 2 in two's complement
def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val


#write_byte############################################################
#writes a byte to the register on the device through i2c
#Param: adr, address of target register
#Param: value, value to write to target register
def write_byte(adr, value):
    bus.write_byte_data(address, adr, value)

#init_magnetometer#####################################################
#Sets the magnetometer settings
#Note: Currently default settings.  For different settings use magnetometer datasheet online
def init_magnetometer():
    bus = smbus.SMBus(1)#Set the correct bus
    address = 0x1e #i2c address of the magnetometer

    write_byte(0, 0b01110000) # Set to 8 samples @ 15Hz
    write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
    write_byte(2, 0b00000000) # Continuous sampling

#read_bearing###########################################################
#Reads the direction the magnetometer is facing
#Return: Magnetometer bearing in degrees (Do no know what reference is)
def read_bearing():
    scale = 0.92 #Used to account for error

    #Scales the x and y input to the correct output
	x_out = read_word_2c(3) * scale
	y_out = read_word_2c(7) * scale

    #Produces the corrent bearing in radians
	bearing  = math.atan2(y_out, x_out)#Output angle in radians from -pi to pi
	if (bearing < 0): #If angle is less than zero, add 2pi to to make angle positive
    		bearing += 2 * math.pi


    bearingDeg = math.degrees(bearing) #Convert angle to degrees
	
    return bearingDeg #Return angle in degrees
