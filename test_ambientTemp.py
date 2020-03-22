import pytest
import os,sys
import AmbientTemp

def test_main(capsys):
    data_pin_connection = 'board.D26'
    temp, humidity = AmbientTemp.readAmbient(data_pin_connection)
    print('Ambient Temperature: ' + str(temp))
    print('Ambient Humidity: ' + str(humidity))
