#!/usr/bin/env python3

""" Display stats on Beer cellar
    Usage:
        python3 cellar.py

"""
import time
import os, sys
import logging
import importlib
import csv

import modules.config.manager as cfg_mgr
import modules.config.logging as logger

def csv_has_header(file):
    """Returns boolean if supplied file has a header

    Required:
    - file (str): full path to csv file
    """
    header = csv.Sniffer()
    has_header = False
    f = open(file, 'r')
    if len(f.readlines()) > 0:
        f.seek(0)
        has_header = header.has_header(f.readline())
    
    return has_header
    

def csv_dict_writer(file, field_names, d):
    """Write a dictionary to a CSV file

    Required
    - file (str): file to write to
    - field_names (list): list of field names of csv
    - d (dict): dictionary of keys and values to write
    """

    with open(file, 'a+', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names, quoting=csv.QUOTE_NONNUMERIC)
        if os.path.exists(file) and csv_has_header(file):
            writer.writerow(d)
        else:
            writer.writeheader()
            writer.writerow(d)

    return

def main():
 
    

    # Set config object
    config = cfg_mgr.ConfigManager()
    
    # Set stats objects
    stats_buffer = {}
    stats_field_names = ['date','time','cellar_name','ambient_temperature','ambient_humidity']
    stats_dir = os.path.expanduser(config.defaults.stats_dir)
    if not os.path.exists(stats_dir):
        os.mkdir(stats_dir)
    stats_file = os.path.join(stats_dir, 'cellar.csv')
    stats_buffer['cellar_name'] = config.cellar.name
    stats_buffer['date'] = time.strftime("%Y-%m-%d", time.localtime())
    stats_buffer['time'] = time.strftime("%H:%M:%S", time.localtime())

    # Set logging objects
    log_buffer = []
    log_dir = os.path.expanduser(config.defaults.log_dir)
    log_file = os.path.join(log_dir, 'cellar.log')
    log_this = logger.load_logger('include-beer.cellar', log_file, config.defaults.debug)
    log_this.debug('Opening cellar')
    log_buffer.append('Opening cellar')
    
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
    log_buffer.append('A/T: ' + str(ambient_temp))
    log_this.debug('Ambient Humidity: ' + str(ambient_humidity))
    log_buffer.append('A/H: ' + str(ambient_humidity))
    

    # clear log_buffer
    log_this.info(' | '.join(map(str, log_buffer)))
    
    # Write stats_buffer only if temp and humidity are integers
    if isinstance(ambient_temp, float) and isinstance(ambient_humidity, float):
        stats_buffer['ambient_humidity'] = ambient_humidity
        stats_buffer['ambient_temperature'] = ambient_temp
        csv_dict_writer(stats_file, stats_field_names, stats_buffer)
    print(stats_buffer)


if __name__ == '__main__':
    main()
