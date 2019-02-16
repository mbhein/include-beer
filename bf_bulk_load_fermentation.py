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
import datetime
import pytz

class props(object):
    def __init__(self,props_file):

        cp = configparser.ConfigParser()
        cp.read(props_file)

        #set Main Properties
        self.api_fermentation_url = cp.get('main','api_fermentation_url')
        self.api_key = cp.get('main','api_key')

def convert_to_utc(local_date_time):
    temp_local_date_time = datetime.datetime.strptime(local_date_time.split(',')[0], '%Y-%m-%d %H:%M:%S')
    timezone = pytz.timezone("UTC")
    utc_date_time = temp_local_date_time.astimezone(timezone)
    return utc_date_time

def read_brew_log():

    with open('./brewlog/pri_winstons_spitfire_b1.log', 'r') as f:
        reader = csv.reader(f, dialect='excel', delimiter='|')
        for row in reader:
            if 4 < len(row):
                # temp_local_datetime = row[0]
                # local_datetime = datetime.datetime.strptime(temp_local_datetime, '%Y-%m-%d %H:%M:%S')
                # timezone = pytz.timezone("Etc/Greenwich")
                utc_datetime = convert_to_utc(row[0])

                print(row[0] + ' ' + utc_datetime.strftime("%Y-%m-%d %H:%M:%S") + ' ' + row[3])


def build_fermentation_JSON():
    fermentation_load = []
    i = 0
    with open('./brewlog/sec_winstons_spitfire_b1.log', 'r') as f:
        reader = csv.reader(f, dialect='excel', delimiter='|')
        for row in reader:
            if 4 < len(row) and row[0].split(':')[1] in ['00','30']:
                utc_datetime = convert_to_utc(row[0])
                stage = row[3].upper().strip()
                if len(row) >= 9:
                    comment = stage + '' + row[8]
                else:
                    comment = stage + '' + row[7]
                entry = { "name": "include-beer",
                         "temp": row[6],
                         "temp_unit": "F",
                         "gravity": "",
                         "gravity_unit": "P",
                         "ph": "",
                         "comment": comment,
                         "beer": "263425",
                         "battery": "",
                         "RSSI": "",
                         "angle": "",
                         "created_at": utc_datetime.strftime("%Y-%m-%d %H:%M:%S")
                        }
                i += 1
                fermentation_load.append(entry)
    return fermentation_load

def post_brew_log():

    api_url = bf_props.api_fermentation_url + '263425'

    headers = {'Content-Type': 'application/json', 'X-API-KEY': bf_props.api_key}

    load = build_fermentation_JSON()

    response = requests.post(api_url, headers=headers, json=load)
    print(response.content.decode('utf-8'))
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return response.status_code


def main():
    #runtime objects
    global bf_props
    bf_config_file = '.brewersfriend.config'
    bf_props = props(bf_config_file)

    post_brew_log()

    #print(build_fermentation_JSON())


if __name__ == '__main__':
    main()
