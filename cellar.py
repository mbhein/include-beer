#!/usr/bin/env python3

""" Display stats on Beer cellar
    Usage:
        python3 cellar.py

"""
import time
import os, sys
import logging
import importlib

import modules.config.manager as cfg_mgr
import modules.config.logging as logger

def main():

    # Set config object
    config = cfg_mgr.ConfigManager()
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Set logging objects
    log_dir = os.path.expanduser(config.defaults.log_dir)
    log_file = os.path.join(log_dir, 'cellar.log')
    log_this = logger.load_logger('include-beer.cellar', log_file, config.defaults.debug)
    log_this.debug('Opening cellar')
    
    # Load ambient sensor module
    ambient_sensor = config.defaults.ambient_sensor
    log_this.debug('Set ambient sensor to: ' + ambient_sensor)
    try: 
        a_sensor = importlib.import_module('modules.sensors.' + ambient_sensor)
    except Exception as e:
        log_this.error('Error loading ambient sensor: ' +
                       ambient_sensor + ' exception: ' + str(e))
    
    # Get ambient temperature and humidity
    ambient_temp, ambient_humidity = a_sensor.read(config.defaults.ambient_pin)
    log_this.debug('Ambient Temperature: ' + str(ambient_temp))
    log_this.debug('Ambient Humidity: ' + str(ambient_humidity))

    



if __name__ == '__main__':
    main()
