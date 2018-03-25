#!/usr/bin/env python3

""" Script to turn RF outlet on|off
    Usage:
        python3 controlRFOutlet.py [on|off]

"""

from subprocess import check_output
import os, sys

def turnOutletOn():
    #Turn outlet on
    #Define our cmd
    cmd = rfOutletDir + '/codesend ' + rfOutletOnCode + ' -l ' + rfOutletPulse

    #try to turn outlet on and write to our controlFile
    try:
        codesendOutput = check_output(cmd, shell=True)

    except:
        pass #need to figure out error handling

    pass #need to implement write log handling for codesendOutput



def turnOutletOff():
    #Turn outlet off
    #Define our cmd
    cmd = rfOutletDir + '/codesend ' + rfOutletOffCode + ' -l ' + rfOutletPulse

    #try to turn outlet off and remove controlFile
    #to ensure outlet is turned off, exec the cmd 3 times
    try:
        for i in range(3):
            codesendOutput += check_output(cmd, shell=True)
            time.sleep(1)
        
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



    if action == 'on':
        turnOutletOn()

    elif action == 'off':
        turnOutletOff()





if __name__ == '__main__':
    main()
