#!/usr/bin/env python3

""" Main script for streaming fermentation stats to 3rd Party
    Usage:
        python3 stream.py



"""
import configparser
import AmbientTemp
import probeTemp
import time
import os, sys
import logging
import modules.brewersfriend.api.api as bf

class get_props(object):
    def __init__(self):

        cp = configparser.ConfigParser()
        cp.read(main_properties)

        #set Main Properties
        self.debug = cp.get('main','debug')
        self.baseDir = cp.get('main','baseDir')
        self.brewLogDir = "{}{}/".format(self.baseDir,cp.get('main','brewLogDir'))

        #brewing Properties
        self.beer_name = cp.get('main','beerName')
        self.action = cp.get('main','action')
        self.brewlog = "{}{}_{}.log".format(self.brewLogDir,self.action,self.beer_name)
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

def check_heat_state():
    #if Heaton is present check_heat_state returns True
    if os.path.exists(props.heaterControlFile):
        return 1
    else:
        return 0

def main():
    #runtime objects
    global main_properties
    global props
    global logger
    main_properties = './properties/main.properties'
    props = get_props()
    brewers_friend_config = 'brewersfriend.cfg'
    bfapi = bf.API(brewers_friend_config,props.brewlog)

    currentDateTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Setup logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    stream_log_file = "{}/stream_{}_{}.log".format(props.brewLogDir, props.action, props.beer_name)
    console_handler_info = logging.StreamHandler()
    console_handler_info.setLevel(logging.INFO)
    console_handler_info.setFormatter(formatter)
    logger.addHandler(console_handler_info)
    file_handler_info = logging.FileHandler(stream_log_file)
    file_handler_info.setLevel(logging.INFO)
    file_handler_info.setFormatter(formatter)
    logger.addHandler(file_handler_info)

    # Our target temp right now is the fermLow temperature
    target_temp = float(props.fermLow)

    # what fermentation stage are we at
    fermentation_stage = props.action

    # Get current ambient temperature
    ambient_temp, ambient_humidity = AmbientTemp.readAmbient(props.ambientPin)

    #Get current probe temperature
    probe_temperature = probeTemp.readProbe(props.probeBaseDir,props.probeDeviceFile)

    # Check if Heating element is on
    heat_check = check_heat_state()
    if heat_check:
        heat_state = "heating"
    else:
        heat_state = "heat off"

    comment = "{} - Target Temp {} - {}".format(fermentation_stage, target_temp, heat_state)

    # Build JSON load
    json_load = bfapi.stream_build_JSON(probe_temperature, comment, target_temp, heat_state, ambient_temp)
    logger.info('JSON load: ' + str(json_load))

    # Post JSON Load
    error_flag, post_response = bfapi.stream_post(json_load)
    logger.info('Post Response: ' + str(error_flag) + ' ' + str(post_response))


if __name__ == '__main__':
    main()
