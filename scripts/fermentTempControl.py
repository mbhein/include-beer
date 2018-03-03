#!/usr/bin/python

# fermentTempControl.py
# Control fermentation temperature

# Take in arguments of min and max temperature
# If one temperature is entered, use it for both min and max


import os, sys
import Adafruit_DHT
import glob
import time as CDT
from subprocess import check_output

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
outputfile='/home/pi/include-beer/scripts/pri_chocolate_pecan_porter.txt'
currentDateTime=CDT.strftime("%Y-%m-%d %H:%M:%S", CDT.localtime())
control_file='/home/pi/include-beer/files/HeatOn'

probeBaseDir = '/sys/bus/w1/devices/'
probe_found = True




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
    #debug area
    currentTemps = 'Probe: ' + str(read_temp()) + ' F Ambient: ' +  str(read_ambient()[0]) + ' F'
    rawTemps = read_temp(), read_ambient()[0]
    #print currentTemps
    #print rawTemps

    if read_temp() < int(temp_min):
        if os.path.exists(control_file):
            temp_status = "Action: Heater already on"
        else:
            temp_status = "Action: Turning Heater on"
            call_controlHeater = check_output('/home/pi/include-beer/scripts/controlHeater.py on', shell=True)
    elif read_temp() > int(temp_max):
        temp_status = "Action: Need to cool vessel"
    else:
        temp_status = "Action: Temperature is perfect"
        if os.path.exists(control_file):
            call_controlHeater = check_output('/home/pi/include-beer/scripts/controlHeater.py off', shell=True)
else:
    currentTemps = 'ERROR ***PROBE not FOUND*** Ambient: ' +  str(read_ambient()[0]) + ' F'
    temp_status = 'Action: Turn off Heater'
    call_controlHeater = check_output('/home/pi/include-beer/scripts/controlHeater.py off', shell=True)

# open output file to append
fo = open(outputfile, 'a')
fo.write(currentDateTime + ' ' + ferment_range + ' ' + ' ' + currentTemps + ' ' + temp_status + '\n')
fo.close()
#print action
#print ferment_range + ' ' + ' ' + currentTemps + ' ' + action

exit()
