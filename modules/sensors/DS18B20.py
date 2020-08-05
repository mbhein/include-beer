#!/usr/bin/env python3

""" Functions to read DS18B20 probe sensor

"""
import os
import glob
import sys
import time

def read_probe_data_file(file):
    """open, read, and return lines of probe data file

    Required:
        file (str): full path of probe data file
    """
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read(probe_id, base_dir, data_file, temp_format='f'):
    """read DS18B20 sensor

    Required:
        probe_id (str): ID of probe to read
        base_dir (str): base dir of probes
        data_file (str): file containing probe data
        temp_format (str, default=f): c or f 

    Returns float if probe is found else string 'Probe not found'
    """

    probe_data_file = base_dir + '/' + probe_id + '/' + data_file
    if os.path.exists(probe_data_file):
        lines = read_probe_data_file(probe_data_file)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_probe_data_file(probe_data_file)
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            raw_temperature = lines[1][equals_pos+2:]
            temperature_c = round(float(raw_temperature) / 1000.0, 2)
            if temp_format == 'f':
                temperature = round(temperature_c * 9.0 / 5.0 + 32.0, 2)
            elif temp_format == 'c':
                temperature = temperature_c
        return temperature
    else:
        return 'Probe not found'
