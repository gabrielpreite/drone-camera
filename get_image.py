from picamera import PiCamera
import numpy as np
import time
import serial
from project_coordinates import proj
from project_coordinates import Coor

camera = PiCamera()
camera.start_preview()
time.sleep(1)
#open serial
ser = serial.Serial('/dev/ttyUSB0',115200)
#while True:
#read serial
#       get GPS and Distance
line = ser.readline()
lat, lon, dist = line.split(';')
gpsPos = lat + " " + lon
distance = int(dist)
alt = 100
#uppertext ='lettura:' + str(i) + ' ' +  str(distance) + ' ' + str(lat) + ' ' + str(lon)
obj = proj(Coor(float(lat), float(lon), float(alt)), distance, Coor(270.0, 180.0, 0))
uppertext = "Drone Coordinates: "+str(lat)+", "+str(lon)+"\nAltitude: "+str(alt)+"cm\n"
bottomtext = "Object Coordinates: "+str(obj[0])+", "+str(obj[1])+"\nDistance: "+str(distance)+"cm\nAltitude: "+str(obj[2])+"cm"
camera.annotate_text = uppertext+bottomtext
print uppertext
print bottomtext
camera.capture('/home/pi/Documents/image.jpg')
time.sleep(2)
camera.stop_preview()
