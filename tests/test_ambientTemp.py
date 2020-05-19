import pytest
import os,sys
import AmbientTemp
import board

def test_main(capsys):
    data_pin = 'Empty'
    temp, humidity = AmbientTemp.readAmbient(data_pin)
    print('Ambient Temperature: ' + str(temp))
    print('Ambient Humidity: ' + str(humidity))
