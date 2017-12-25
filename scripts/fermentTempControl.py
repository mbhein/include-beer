#!/usr/bin/python

# fermentTempControl.py
# Control fermentation temperature

# Take in arguments of min and max temperature
# If one temperature is entered, use it for both min and max


import os, sys
import Adafruit_DHT
import glob
import time as CDT


argslen = len(sys.argv)

if argslen < 2:
    print "no arguments entered"
    exit()
elif argslen == 2:
    temp_max = temp_min = sys.argv[1]
elif argslen == 3:
    if sys.argv[1] > sys.argv[2]:
        temp_max = sys.argv[1]
        temp_min = sys.argv[2]
    else:
        temp_max = sys.argv[2]
        temp_min = sys.argv[1]
elif argslen > 3:
    print "too many arguments entered"
    exit()

ferment_range = 'Max: ' + temp_max + ' Min: ' + temp_min

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# declare and set our variables
outputfile='/home/pi/scripts/output_FermentTempControl.txt'
currentDateTime=CDT.strftime("%Y-%m-%d %H:%M:%S", CDT.localtime())

probeBaseDir = '/sys/bus/w1/devices/'
probeDeviceFolder = glob.glob(probeBaseDir + '28*')[0]
probeDeviceFile = probeDeviceFolder + '/w1_slave'



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

#debug area
currentTemps = 'Probe: ' + str(read_temp()) + ' F Ambient: ' +  str(read_ambient()[0]) + ' F'
rawTemps = read_temp(), read_ambient()[0]
#print currentTemps
#print rawTemps

if read_temp() < temp_min:
    action = "Action: Power on heater"
elif read_temp > temp_max:
    action = "Action: Need to cool vessel"
else:
    action = "Action: Temperature is perfect"

# open output file to append
fo = open(outputfile, 'a')
fo.write(currentDateTime + ' ' + ferment_range + ' ' + ' ' + currentTemps + ' ' + action + '\n')
fo.close()
#print action
#print ferment_range + ' ' + ' ' + currentTemps + ' ' + action

exit()
