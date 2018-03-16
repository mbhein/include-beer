#!/usr/bin/python

# controlHeater.py
# Turn heater on and off

from subprocess import check_output
import os, sys
import time as CDT

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

### declare and set our variables
# - moved to properties file
# outputFile='/home/pi/include-beer/scripts/pri_chocolate_pecan_porter.txt'

# +/- need to figure out how to set common timestamp across scripts
currentDateTime=CDT.strftime("%Y-%m-%d %H:%M:%S", CDT.localtime())

# - move to properties file
control_file='/home/pi/include-beer/files/HeatOn'

#codesend variable
if action == 'on':
    heatAction = '~/rfoutlet/codesend 5256451 -l 168'
    with open(control_file, "w") as fw:
        fw.write(currentDateTime)
    codesend_output = check_output(heatAction, shell=True)

elif action == 'off':
    heatAction = '~/rfoutlet/codesend 5256460 -l 168'
    if os.path.exists(control_file):
        os.remove(control_file)
    else:
        action = action + ' HeatOn not there'


#print codesend_output
codesend_output_1 = check_output(heatAction, shell=True)
CDT.sleep(1)
codesend_output_2 = check_output(heatAction, shell=True)
CDT.sleep(1)
codesend_output_3 = check_output(heatAction, shell=True)
codesend_output = codesend_output_1 + ' ' + codesend_output_2 + ' ' + codesend_output_3
# open output file to append
fo = open(outputfile, 'a')
fo.write(currentDateTime + ' Heater: ' + action + ' ' + codesend_output)
fo.close()

exit()
