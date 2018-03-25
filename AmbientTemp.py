#!/usr/bin/env python3

""" script for getting Ambient tempature and humidity
    Usage:
        python3 AmbientTemp.py

 Requires DHT11 sensor for RPi

"""

import Adafruit_DHT


def readAmbient(pin):
    #Read Ambient Temp/Humidity from DHT11
    humidity, temp = Adafruit_DHT.read_retry(11, pin)
    temp = temp * 9/5.0 + 32
    return temp, humidity



def main():
    defaultPin = 25
    ambientTemp, ambientHumidity = readAmbient(defaultPin)
    print('Ambient Temperature: ' + ambientTemp)
    print('Ambient Humidity: ' + ambientHumidity)


if __name__ == '__main__':
    main()
