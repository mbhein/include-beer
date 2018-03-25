#!/usr/bin/env python3

""" script for getting DS18B20 probe tempature
    Usage:
        python3 probeTemp.py

 Requires DS18B20 probe

"""

import os, sys
import glob

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')




def readTempRaw():
    #Get raw temp from DS18B20
    f = open(probeDeviceFile, 'r')
    lines = f.readlines()
    f.close()
    return lines

#Process raw temp from DS18B20
def readTemp(fc):
    lines = readTempRaw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readTempRaw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        probe_temp_string = lines[1][equals_pos+2:]
        if fc == 'F':
            probeTemp = round(probe_temp_c * 9.0 / 5.0 + 32.0,2)
        elif fc == 'C':
            probeTemp = round(float(probe_temp_string) / 1000.0,2)
        else:
            probeTemp = round(probe_temp_c * 9.0 / 5.0 + 32.0,2)
    return probeTemp


def main():
    probeFound = True
    probeBaseDir = '/sys/bus/w1/devices/'
    try:
        probeDeviceFolder = glob.glob(probeBaseDir + '28*')[0]
    except IndexError:
        probeFound = False

    if probeFound:
        probeDeviceFile = probeDeviceFolder + '/w1_slave'
        try:
            probeTemp = readTemp(F)
        except IOError:
            probeTemp = 'ISSUE with PROBE'
    else:
        probeTemp = 'PROBE not found'


    print('Probe tempature: ' + str(probeTemp))

if __name__ == '__main__':
    main()
