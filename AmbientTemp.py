#!/usr/bin/env python3

""" script for getting Ambient tempature and humidity
    Usage:
        python3 AmbientTemp.py

 Requires DHT11 sensor for RPi

"""
import board
import adafruit_dht

def readAmbient(data_pin_connection):
    dht_device = adafruit_dht.DHT11(data_pin_connection)
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dht_device.humidity
        return temperature_f, humidity
    except RuntimeError as error:
        print('Errors happen fairly often, DHT''s are hard to read, just keep going after you read the following error msg:')
        print(error.args[0])
        exit



def main():
    data_pin_connection = board.D26
    ambientTemp, ambientHumidity = readAmbient(data_pin_connection)
    print('Ambient Temperature: ' + str(ambientTemp))
    print('Ambient Humidity: ' + str(ambientHumidity))


if __name__ == '__main__':
    main()
