#!/usr/bin/env python3

""" Functions to read DHT11 Ambient temperature sensor

"""
import board
import adafruit_dht
import sys


def read(data_pin, temp_format='f'):
    """read ambient sensor

    Required:
        data_pin (int): pin data is on
        temp_format (str, default=f): c or f 
    """
    if isinstance(data_pin, str) and data_pin == 'Empty':
        data_pin = eval('board.Empty')
    elif isinstance(data_pin, int):
        data_pin = eval('board.D' + str(data_pin))
    elif isinstance(data_pin, str):
        data_pin = eval('board.D' + data_pin)
    else:
        return "Data pin supplied is not a valid value", str(data_pin)
    dht_device = adafruit_dht.DHT11(data_pin)
    try:
        # by default the device returns c
        temperature = dht_device.temperature
        if temp_format == 'f':
            temperature = temperature * (9 / 5) + 32
        humidity = dht_device.humidity
        return temperature, humidity
    except RuntimeError as error:
        # TODO: figure out better error handling and message return
        # print('Errors happen fairly often, DHT''s are hard to read, just keep going after you read the following error msg:')
        # print(error.args[0])
        return "DHT read error", error.args[0]
