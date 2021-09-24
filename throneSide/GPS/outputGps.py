import serial #导入serial模块
import pynmea2
import time

openDetail = False

ser = serial.Serial("/dev/ttyUSB0",9600)#打开串口，存放到ser中，/dev/ttyUSB0是端口名，9600是波特率

def getMyGpsOnce():
    line = ser.readline()
    if line.startswith('$GNRMC'):
        rmc = pynmea2.parse(line)
        lat=float(rmc.lat)/100
        lon=float(rmc.lon)/100
        if (openDetail):
            print("Latitude:  ", lat)
            print("Longitude: ", lon)
        return [lon,lat]
    return False
        