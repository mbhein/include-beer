#!/usr/bin/env python3

""" fermentation beer
    Usage:
        python3 fermentation.py

"""
import time
from datetime import datetime
import os, sys
import logging
import importlib
import csv

import modules.config.manager as cfg_mgr
import modules.config.logging as logger
from modules.utils.dicts import DotNotation as DotNotation


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
    stats_field_names = ['timestamp','fermentation_stage','vessel','vessel_temperature']
    stats_dir = os.path.expanduser(config.defaults.stats_dir)
    if not os.path.exists(stats_dir):
        os.mkdir(stats_dir)
    stats_file = os.path.join(stats_dir, 'fermentation.csv')
    stats_buffer['fermentation_stage'] = config.fermentation.stage
    stats_date = datetime.now()
    stats_buffer['timestamp'] = stats_date.isoformat() # ("%Y-%m-%d", time.localtime())


    # Set logging objects
    log_buffer = []
    log_dir = os.path.expanduser(config.defaults.log_dir)
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    log_file = os.path.join(log_dir, 'fermentation.log')
    log_this = logger.load_logger('include-beer.fermentation', log_file, config.defaults.debug)
    log_this.debug('Explore fermentation')
    log_buffer.append('Explore fermentation')
    
    # Loop on each Vessel in configuration
    for _k, _v in config.vessels.items():
        vessel_log_buffer = []
        vessel_log_buffer = log_buffer.copy()
        #vessel_log_bufferappend(log_buffer)
        vessel = DotNotation(eval(_v))
        _name = vessel.name
        _probe = vessel.probe.split('.')[0]
        _probe_id = vessel.probe.split('.')[1]
        log_this.debug('Vessel: ' + _name)
        vessel_log_buffer.append(_name)
        stats_buffer['vessel'] = _name
        log_this.debug('Set vessel probe to: ' + _probe)

        # Load vessels probe
        try:
            a_probe = importlib.import_module('modules.sensors.' + _probe)
        except Exception as e:
            log_this.error('Error loading vessel probe: ' +
                           _probe + ' exception: ' + str(e))
        
        # Get vessel temperature
        _vessel_temp = a_probe.read(_probe_id, config.DS18B20.base_dir, config.DS18B20.data_file)
        log_this.debug('Vessel temperature: ' + str(_vessel_temp))
        vessel_log_buffer.append('Vessel temperature: ' + str(_vessel_temp))
        # clear log_buffer
        log_this.info(' | '.join(map(str, vessel_log_buffer)))
        
        # Write stats_buffer only if temperature is numeric
        if isinstance(_vessel_temp, (float, int)):
            stats_buffer['vessel_temperature'] = _vessel_temp
            csv_dict_writer(stats_file, stats_field_names, stats_buffer)

        if vessel.control_temperature:
            #TODO add code to control vessel temperature
            pass

if __name__ == '__main__':
    main()
