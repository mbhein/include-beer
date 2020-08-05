import pytest
import os,sys
import modules.sensors.DS18B20 as sensor


def test_found(capsys):
    probe_id = '28-2018'
    base_dir = './SDK'
    data_file = 'w1_slave'
    temp = sensor.read(probe_id, base_dir, data_file)
    assert type(temp) is float
    print('Sensor Temperature: ' + str(temp))


def test_not_found(capsys):
    probe_id = '28-2019'
    base_dir = './SDK'
    data_file = 'w1_slave'
    temp = sensor.read(probe_id, base_dir, data_file)
    assert type(temp) is str
    print('Sensor Temperature: ' + str(temp))
