#!/usr/bin/env python3

""" Script to turn heating element on|off
    Usage:
        python3 controlHeater.py [on|off]

"""

from subprocess import check_output
import os, sys
import time

def turnHeatOn():
    #Turn heater on
    #Define our heaterAction
    heaterAction = rfOutletDir + '/codesend ' + rfOutletOnCode + ' -l ' + rfOutletPulse

    #try to turn heater on and write to our controlFile
    try:
        codesendOutput = check_output(heaterAction, shell=True)
        with open(controlFile, "w") as fw:
            fw.write(currentDateTime)
    except:
        pass #need to figure out error handling

    pass #need to implement write log handling for codesendOutput



def turnHeatOff():
    #Turn heater off
    #Define our heaterAction
    heaterAction = rfOutletDir + '/codesend ' + rfOutletOffCode + ' -l ' + rfOutletPulse

    #try to turn heater off and remove controlFile
    #to ensure heater is turned off, exec the heaterAction 3 times
    try:
        for i in range(3):
            codesendOutput += check_output(heaterAction, shell=True)
            time.sleep(1)
        if os.path.exists(controlFile):
            os.remove(controlFile)
        else:
            pass #need to define output
    except:
        pass #need to figure out error handling

    pass #need to implement write log handling for codesendOutput


def main():
    #Process argument
    argslen = len(sys.argv)

    if argslen < 2:
        print "no arguments entered"
        exit()
    elif argslen == 2:
        action = sys.argv[1]
    elif argslen > 2:
        print "too many arguments entered"
        exit()

    # +/- need to figure out how to set common timestamp across scripts
    currentDateTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


    if action == 'on':
        turnHeatOn()

    elif action == 'off':
        turnHeatOff()

    # open output file to append
    fo = open(outputFile, 'a')
    fo.write(currentDateTime + ' Heater: ' + action + ' ' + codesend_output)
    fo.close()



if __name__ == '__main__':
    main()
