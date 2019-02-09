#!/usr/bin/env python3

""" Used to mimic Adafruit_DHT plugin

    Usage:
        python3 Adafruit_DHT.py

    Adafruit_DHT.read_retry(11, pin) returns 60 and 58

"""

def read_retry(x,y):
    humidity = 58
    temp = 20
    return humidity, temp



def main():
    x = 11
    y = 25
    ambientTemp, ambientHumidity = read_retry(x,y)
    print('Ambient Temperature: ' + str(ambientTemp))
    print('Ambient Humidity: ' + str(ambientHumidity))


if __name__ == '__main__':
    main()
