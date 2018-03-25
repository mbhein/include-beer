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




def readTempRaw(probe):
    #Get raw temp from DS18B20
    f = open(probe, 'r')
    lines = f.readlines()
    f.close()
    return lines

#Process raw temp from DS18B20
def readTemp(probe,fc):
    lines = readTempRaw(probe)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readTempRaw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        probeTempC = lines[1][equals_pos+2:]
        probeTempC = round(float(probeTempC) / 1000.0,2)
        if fc == 'F':
            probeTemp = round(probeTempC * 9.0 / 5.0 + 32.0,2)
        elif fc == 'C':
            probeTemp = probeTempC
        else:
            probeTemp = round(probeTempC * 9.0 / 5.0 + 32.0,2)
    return probeTemp


def readProbe():
    probeFound = True
    probeBaseDir = '/sys/bus/w1/devices/'
    try:
        probeDeviceFolder = glob.glob(probeBaseDir + '28*')[0]
    except IndexError:
        probeFound = False

    if probeFound:
        probeDeviceFile = probeDeviceFolder + '/w1_slave'
        try:
            probeTemp = readTemp(probeDeviceFile,'F')
        except IOError:
            probeTemp = 'ISSUE with PROBE'
    else:
        probeTemp = 'PROBE not found'


    return probeTemp

def main():
    probeTemp = readProbe()
    print('Probe temperature: ' + str(probeTemp))

if __name__ == '__main__':
    main()
