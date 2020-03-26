#!/usr/bin/env python3

""" script for getting Ambient tempature and humidity
    Usage:
        python3 AmbientTemp.py

 Requires DHT11 sensor for RPi

"""
import board
import adafruit_dht
import sys

def readAmbient(data_pin):
    if isinstance(data_pin, str) and data_pin == 'Empty':
        data_pin = eval('board.Empty')
    elif isinstance(data_pin, int):
        data_pin = eval('board.D' + str(data_pin))
    else:
        print('Data pin supplied is not a valid value')
        sys.exit(1)
    dht_device = adafruit_dht.DHT11(data_pin)
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dht_device.humidity
        return temperature_f, humidity
    except RuntimeError as error:
        # TODO: figure out better error handling and message return
        print('Errors happen fairly often, DHT''s are hard to read, just keep going after you read the following error msg:')
        print(error.args[0])
        sys.exit(1)


def main():
    data_pin = 6
    try:
        ambientTemp, ambientHumidity = readAmbient(data_pin)
        print('Ambient Temperature: ' + str(ambientTemp))
        print('Ambient Humidity: ' + str(ambientHumidity))
    except Exception as e:
        # TODO: figure out better error handling and message return
        pass


if __name__ == '__main__':
    main()
