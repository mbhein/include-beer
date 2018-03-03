#!/usr/bin/python

# get-envTemp.py gets the ambient tempature via DHT11 and
#	vessel temperature via  the DS18B20


import os, sys
import Adafruit_DHT
import glob
import time


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
probe_found = True
probeBaseDir = '/sys/bus/w1/devices/'


#Get raw temp from DS18B20
def read_temp_raw():
    f = open(probeDeviceFile, 'r')
    lines = f.readlines()
    f.close()
    return lines

#Process raw temp from DS18B20
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        probe_temp_string = lines[1][equals_pos+2:]
        probe_temp_c = round(float(probe_temp_string) / 1000.0,2)
        probe_temp_f = round(probe_temp_c * 9.0 / 5.0 + 32.0,2)
        return probe_temp_f

#Read Ambient Temp/Humidity from DHT11
def read_ambient():
    ambient_humidity, ambient_temp = Adafruit_DHT.read_retry(11, 25)
    ambient_temp = ambient_temp * 9/5.0 + 32
    return ambient_temp, ambient_humidity

try:
    probeDeviceFolder = glob.glob(probeBaseDir + '28*')[0]
except IndexError:
    probe_found = False

if probe_found:
    probeDeviceFile = probeDeviceFolder + '/w1_slave'
    try:
        currentTemps = 'Probe: ' + str(read_temp()) + ' F Ambient: ' +  str(read_ambient()[0]) + ' F '
    except IOError:
        currentTemps = 'ISSUE with PROBE'
    try:
        rawTemps = read_temp(), read_ambient()[0]
    except IOError:
        rawTemps = 'ISSUE with PROBE'

else:
    currentTemps = 'PROBE not found'
    rawTemps = 'PROBE not found'

print currentTemps
print rawTemps
exit()
