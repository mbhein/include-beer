import pytest
import os,sys
import modules.sensors.DHT11 as sensor
import board

def test_main(capsys):
    data_pin = 'Empty'
    temp, humidity = sensor.read(data_pin)
    print('Ambient Temperature: ' + str(temp))
    print('Ambient Humidity: ' + str(humidity))
