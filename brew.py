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
import controlRFOutlet
import time
import os, sys
import logging

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
        self.brewlog = "{}{}_{}.log".format(self.brewLogDir,self.action,cp.get('main','beerName'))
        self.fermHigh = cp.get('main','fermHigh')
        self.fermLow = cp.get('main','fermLow')
        self.heaterControlFile = "{}{}".format(self.baseDir,cp.get('main','controlFile'))

        #set Ambient properites
        self.ambientPin = cp.get('ambient','pin')

        #set vessel propbe properites
        if os.getenv('include_beer_probe_device_base',0):
            self.probeBaseDir = os.environ['include_beer_probe_device_base']
        else:
            self.probeBaseDir = cp.get('vesselProbe','probeBaseDir')
        self.probeDeviceFile = cp.get('vesselProbe','probeDeviceFile')

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


def turnHeatOn():
    #Turn heat on by turning outlet on and creating heaterControlFile
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    codeSendOutput = ""

    failure, codeSendOutput = controlRFOutlet.turnOutletOn(mainProps.rfOutletDir,mainProps.rfOutletOnCode,mainProps.rfOutletPulse)
    logBuffer.append(codeSendOutput)
    logger.debug("turnHeatOn output: " + codeSendOutput)
    if (failure):
        error = 1
        flushLogBuffer(error)
        exit()
    else:
        try:
            os.makedirs(os.path.dirname(mainProps.heaterControlFile), exist_ok=True)
            with open(mainProps.heaterControlFile, "w") as fw:
                fw.write(now)
        except Exception as e:
            logger.error("error creating " + mainProps.heaterControlFile + " - " + str(e))

def turnHeatOff():
    #Turn heat off by turning outlet off and remove heaterControlFile
    codeSendOutput = ""

    failure, codeSendOutput = controlRFOutlet.turnOutletOff(mainProps.rfOutletDir,mainProps.rfOutletOffCode,mainProps.rfOutletPulse)
    logBuffer.append(codeSendOutput)
    logger.debug("turnHeatOff output: " + codeSendOutput)
    if (failure):
        error = 1
        flushLogBuffer(error)
        exit()
    else:
        try:
            if os.path.exists(mainProps.heaterControlFile):
                os.remove(mainProps.heaterControlFile)
            else:
                logBuffer.append(mainProps.heaterControlFile + " didn't exist")
        except Exception as e:
            logger.error("error deleting " + mainProps.heaterControlFile + " - " + str(e))

def checkHeatOn():
    #if Heaton is present checkHeatOn returns True
    if os.path.exists(mainProps.heaterControlFile):
        return 1
    else:
        return 0

def flushLogBuffer(error=0):
    if (mainProps.debug == 'True'):
        logger.debug(' | '.join(map(str,logBuffer)))
    elif error:
        logger.error(' | '.join(map(str,logBuffer)))
    else:
        logger.info(' | '.join(map(str,logBuffer)))

def main():
    #runtime objects
    global mainPropsFile
    global mainProps
    global logger
    global logBuffer
    mainPropsFile = './properties/main.properties'
    mainProps = getProps()


    currentDateTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    logBuffer = list()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

    if (mainProps.debug == 'True'):
        chD = logging.StreamHandler()
        chD.setLevel(logging.DEBUG)
        chD.setFormatter(formatter)
        logger.addHandler(chD)
        fhD = logging.FileHandler(mainProps.brewlog)
        fhD.setLevel(logging.DEBUG)
        fhD.setFormatter(formatter)
        logger.addHandler(fhD)
    # else:
        # chD = logging.NullHandler()


    chI = logging.StreamHandler()
    chI.setLevel(logging.INFO)
    chI.setFormatter(formatter)
    logger.addHandler(chI)
    fhI = logging.FileHandler(mainProps.brewlog)
    fhI.setLevel(logging.INFO)
    fhI.setFormatter(formatter)
    logger.addHandler(fhI)


    #make it easy on us
    fermHigh = float(mainProps.fermHigh)
    fermLow = float(mainProps.fermLow)

    #so what are we doing:
    action = mainProps.action
    logBuffer.append(action)
    logger.debug('action = ' + action)

    #Get current ambient temperature
    ambientTemp, ambientHumidity = AmbientTemp.readAmbient(mainProps.ambientPin)
    logBuffer.append(ambientTemp)
    logBuffer.append(ambientHumidity)
    logger.debug('Ambient T/H ' + str(ambientTemp) + '/' + str(ambientHumidity))


    #Get current probe temperature
    probeTemperature = probeTemp.readProbe(mainProps.probeBaseDir,mainProps.probeDeviceFile)
    logBuffer.append(probeTemperature)
    logger.debug('Probe: ' + str(probeTemperature))

    if isinstance(probeTemperature,float):
        if action == 'pri':

            heatsOn = checkHeatOn()

            if probeTemperature < fermLow:
                if heatsOn:
                    actionMsg = 'Heats already on'

                else:
                    actionMsg = 'We need to heat things up'
                    turnHeatOn()

            elif probeTemperature > fermHigh:
                #if temperature above fermHigh turn cooler on
                actionMsg = 'We need to cool things down'
                if heatsOn:
                    actionMsg += ' - Heats on - turn it off'
                    turnHeatOff()


            else:
                actionMsg = 'Temperature is perfect'
                if heatsOn:
                    actionMsg += ' - Heats on - turn it off'
                    turnHeatOff()

        elif action == 'sec':
            pass

        logBuffer.append(actionMsg)
        logger.debug(actionMsg)

    else:
        logger.debug('**** probe returned string: ' + probeTemperature)

    flushLogBuffer()



if __name__ == '__main__':
    main()
