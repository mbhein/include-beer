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

        #set Ambient properites
        self.ambientPin = cp.get('ambient','pin')

        #set Heater Properties
        self.rfOutletDir = cp.get('heater','rfOutletDir')
        self.rfOutletPulse = cp.get('heater','rfOutletPulse')
        self.rfOutletOnCode = cp.get('heater','rfOutletOnCode')
        self.rfOutletOffCode = cp.get('heater','rfOutletOffCode')
        self.heaterControlFile = "{}{}".format(self.baseDir,cp.get('heater','controlFile'))

        return

    def __iter__(self):
        return self

    def __next__(self):
        return self

def printProps(props):
    print(props.brewlog)

def main():
    #runtime objects
    global mainPropsFile
    global mainProps
    mainPropsFile = './properties/main.properties'
    mainProps = getProps()
    if mainProps.debug:
        printProps(mainProps)

    #so what are we doing:
    action = mainProps.action
    print('action = ' + action)

    #Get current ambient temperature
    ambientTemp, ambientHumidity = AmbientTemp.readAmbient(mainProps.ambientPin)
    print('Ambient Temperature: ' + str(ambientTemp))
    print('Ambient Humidity: ' + str(ambientHumidity))

    if action == 'pri':
        print('Primary fermentation')
        #what we will do here is read in probe temperature
        #if temperature below fermLow turn heater on
        #if temperature above fermHigh turn cooler on

        #get current probe tempature
        probeTempature = probeTemp()
        print(probeTempature)



if __name__ == '__main__':
    main()
