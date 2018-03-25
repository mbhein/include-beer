#!/usr/bin/env python3

""" Main script for brewing
    Usage:
        python3 brew.py

 Currently used only to control primary fermentation temperatures
 and record secondary/tertiary fermentation temperatures

"""
import configparser
import AmbientTemp
import probeTemp
import time
import os, sys

class getProps(object):
    def __init__(self):

        cp = configparser.ConfigParser()
        cp.read(mainPropsFile)

        #set Main Properties
        self.debug = cp.get('main','debug')
        self.baseDir = cp.get('main','baseDir')
        self.brewLogDir = "{}{}/".format(self.baseDir,cp.get('main','brewLogDir'))

        #brewing Properties
        self.action = cp.get('main','action')
        self.brewlog = "{}{}_{}.txt".format(self.brewLogDir,self.action,cp.get('main','beerName'))
        self.fermHigh = cp.get('main','fermHigh')
        self.fermLow = cp.get('main','fermLow')
        self.heaterControlFile = "{}{}".format(self.baseDir,cp.get('main','controlFile'))

        #set Ambient properites
        self.ambientPin = cp.get('ambient','pin')

        #set RF Outlet Properties
        self.rfOutletDir = cp.get('RFOutlet','rfOutletDir')
        self.rfOutletPulse = cp.get('RFOutlet','rfOutletPulse')
        self.rfOutletOnCode = cp.get('RFOutlet','rfOutletOnCode')
        self.rfOutletOffCode = cp.get('RFOutlet','rfOutletOffCode')


        return

    def __iter__(self):
        return self

    def __next__(self):
        return self

def printProps(props):
    logWrite(props.brewlog)

def logWrite(msg):
    msg = str(msg)
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(now + ' - ' + msg)

def turnHeatOn():
    #Turn heat on by turning outlet on and creating heaterControlFile
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(mainProps.heaterControlFile, "w") as fw:
        fw.write(now)

def turnHeatOff():
    #Turn heat off by turning outlet off and remove heaterControlFile
    if os.path.exists(mainProps.heaterControlFile):
        os.remove(mainProps.heaterControlFile)
    else:
        pass #need to define output

def main():
    #runtime objects
    global mainPropsFile
    global mainProps
    mainPropsFile = './properties/main.properties'
    mainProps = getProps()
    if mainProps.debug:
        printProps(mainProps)

    #make it easy on us
    fermHigh = float(mainProps.fermHigh)
    fermLow = float(mainProps.fermLow)

    #so what are we doing:
    action = mainProps.action
    logWrite('action = ' + action)

    #Get current ambient temperature
    ambientTemp, ambientHumidity = AmbientTemp.readAmbient(mainProps.ambientPin)
    logWrite('Ambient Temperature: ' + str(ambientTemp))
    logWrite('Ambient Humidity: ' + str(ambientHumidity))

    #Get current probe temperature
    probeTemperature = probeTemp.readProbe()
    logWrite('Probe tempature: ' + str(probeTemperature))

    if action == 'pri':
        logWrite('Primary fermentation')
        if probeTemperature < fermLow:
            #if temperature below fermLow turn heater on
            logWrite('We need heat things up')

        elif probeTemperature > fermHigh:
            #if temperature above fermHigh turn cooler on
            logWrite('We need to cool things down')

        else:
            logWrite('Temperature is just fine')

    if action == 'sec'
        logWrite('Secondary fermentation')
    


if __name__ == '__main__':
    main()
