
import serial
import pynmea2
import time
ser = serial.Serial("/dev/ttyAMA0",9600)
while True:
    line = ser.readline()
    if line.startswith('$GNRMC'):
        rmc = pynmea2.parse(line)
        print ("Latitude:  ", float(rmc.lat)/100)
        print ("Longitude: ", float(rmc.lon)/100)
        break 