import pytest
import os,sys
import modules.sensors.DS18B20 as sensor


def test_found(capsys):
    kwargs = { 'serial_number': '28-2018', 
        'base_dir': './SDK',
        'data_file': 'w1_slave',
        'temperature_scale': 'f'
        }
    temp = sensor.read(**kwargs)
    assert type(temp) is float
    print('Sensor Temperature: ' + str(temp))


def test_not_found(capsys):
    kwargs = {'serial_number': '28-2020',
              'base_dir': './SDK',
              'data_file': 'w1_slave',
              'temperature_scale': 'f'
              }
    temp = sensor.read(**kwargs)
    assert type(temp) is str
    print('Sensor Temperature: ' + str(temp))
