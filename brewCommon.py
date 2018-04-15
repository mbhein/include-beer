#!/usr/bin/env python3

""" Common Classes/Functions for brewing
    Usage:
        python3 brewCommon.py


"""

import configparser

class getProps(object):
    def __init__(self,propsFile):

        cp = configparser.ConfigParser()
        cp.read(propsFile)

        #set Main Properties
        self.debug = cp.get('main','debug')
        self.baseDir = cp.get('main','baseDir')
        #self.brewLogDir = "{}{}/".format(self.baseDir,cp.get('main','brewLogDir'))
        self.brewLogDir = cp.get('main','brewLogDir')

        #brewing Properties
        self.action = cp.get('main','action')
        self.beerName = cp.get('main','beerName')
        self.brewlog = ".{}/{}_{}.txt".format(self.brewLogDir,self.action,cp.get('main','beerName'))
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

if __name__ == '__main__':
    main()
