#!/usr/bin/env python3

""" Used to mimic adafruit_dht module

    Usage:
        python3 adafruit_dht.py

"""

class DHT11(object):
    def __init__(self, data_pin=None):
        self.temperature = 20
        self.humidity = 58
