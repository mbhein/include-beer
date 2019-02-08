#!/usr/bin/env python3

""" Load into Brewer's Friend Beer Session Log data
    Usage:
        python3 bf_stream_api_load.py

    python modules
        sudo pip install requests

    load api_url with key from local .brewersfriend.config

    Put together JSON POST data
    Example data set
    {
     "name": "include-beer",
     "temp": 22.2,
     "temp_unit": "F",
     "gravity": "",
     "gravity_unit": "P",
     "ph": "",
     "comment": "",
     "beer": "",
     "battery": 3.588112,
     "RSSI": "",
     "angle": ""
    }


"""
import configparser
import json
import requests
import csv

class getProps(object):
    def __init__(self,props_file):

        cp = configparser.ConfigParser()
        cp.read(props_file)

        #set Main Properties
        self.api_url = cp.get('main','api_url')

def readBrewLog():

    with open('./brewlog/pri_unit_test.log.max', 'r') as f:
        reader = csv.reader(f, dialect='excel', delimiter='|')
        for row in reader:
            if 4 < len(row):
                print(row)

def post_brew_log():

    api_url = bf_props.api_url

    headers = {'Content-Type': 'application/json'}

    entry = { "name": "include-beer",
             "temp": 53.6,
             "temp_unit": "F",
             "gravity": "",
             "gravity_unit": "P",
             "ph": "",
             "comment": "Final Temperature",
             "beer": "263425",
             "battery": "",
             "RSSI": "",
             "angle": ""
            }

    response = requests.post(api_url, headers=headers, json=entry)
    print(response.content.decode('utf-8'))
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def main():
    #runtime objects
    global bf_props
    bf_config_file = '.brewersfriend.config'
    bf_props = getProps(bf_config_file)

    print(bf_props.api_url)

    readBrewLog()

if __name__ == '__main__':
    main()
