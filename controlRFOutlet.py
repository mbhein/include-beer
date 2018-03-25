#!/usr/bin/env python3

""" Script to turn RF outlet on|off
    Usage:
        python3 controlRFOutlet.py [on|off]

"""

from subprocess import check_output
import os, sys

def turnOutletOn(rfOutletDir,rfOutletOnCode,rfOutletPulse):
    #Turn outlet on
    #Define our cmd
    cmd = rfOutletDir + '/codesend ' + rfOutletOnCode + ' -l ' + rfOutletPulse

    #try to turn outlet on and write to our controlFile
    try:
        codeSendOutput = check_output(cmd, shell=True)

    except:
        print('exception occurred turning outlet on')

    pass #need to implement write log handling for codesendOutput

    return codeSendOutput

def turnOutletOff(rfOutletDir,rfOutletOffCode,rfOutletPulse):
    #Turn outlet off
    #Define our cmd
    cmd = rfOutletDir + '/codesend ' + rfOutletOffCode + ' -l ' + rfOutletPulse

    #try to turn outlet off and remove controlFile
    #to ensure outlet is turned off, exec the cmd 3 times
    try:
        for i in range(3):
            codeSendOutput += check_output(cmd, shell=True)
            time.sleep(1)

    except:
        print('exception occurred turning outlet off')

    pass #need to implement write log handling for codesendOutput

    return codeSendOutput

def main():
    #Process argument
    argslen = len(sys.argv)

    if argslen < 2:
        print(no arguments entered)
        exit()
    elif argslen == 2:
        action = sys.argv[1]
    elif argslen > 2:
        print(too many arguments entered)
        exit()

    #runtime objects
    global propsFile
    global props
    propsFile = './properties/main.properties'
    cp = configparser.ConfigParser()
    cp.read(propsFile)

    #set RF Outlet Properties
    props.rfOutletDir = cp.get('RFOutlet','rfOutletDir')
    props.rfOutletPulse = cp.get('RFOutlet','rfOutletPulse')
    props.rfOutletOnCode = cp.get('RFOutlet','rfOutletOnCode')
    self.rfOutletOffCode = cp.get('RFOutlet','rfOutletOffCode')

    #print RF Outlet properites
    print('RFOutlet ' +  props.rfOutletDir)
    print('RFOutlet Pulse ' +  props.rfOutletPulse)
    print('RFOutlet On code' +  props.rfOutletOnCode)
    print('RFOutlet Off code' +  props.rfOutletOffCode)

    #print Actions
    print('Action ' + action)

    if action == 'on':
        turnOutletOn(props.rfOutletDir,props.rfOutletOnCode,props.rfOutletPulse)

    elif action == 'off':
        turnOutletOff(props.rfOutletDir,props.rfOutletOffCode,props.rfOutletPulse)

    else:
        print('Action isn''t recongized, use: on|off')

    return


if __name__ == '__main__':
    main()
