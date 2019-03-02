#!/usr/bin/env python3

""" Base API module for Brewer's Friend Integration
    Usage:
        python3 bf_stream_api_load.py

    python modules
        sudo pip install requests

    Functions
        post(url,headers,load): post data to Brewer's Friend and return response

"""
import configparser
import json
import requests
import os
import csv
import datetime
import pytz


class API(object):
    def __init__(self,config_file,log_file=None):

        cp = configparser.ConfigParser()
        cp.read(config_file)

        #set Main Properties
        self.log_file = log_file
        self.api_fermentation_url = cp.get('main','api_fermentation_url')

        # Allow override
        if os.getenv('include_beer_brewersfriend_brew_session_id',0):
            self.brew_session_id = os.environ['include_beer_brewersfriend_brew_session_id']
        else:
            self.brew_session_id = cp.get('main','brew_session_id')

        # Allow override
        if os.getenv('include_beer_brewersfriend_api_key',0):
            self.api_key = os.environ['include_beer_brewersfriend_api_key']
        else:
            self.api_key = cp.get('main','api_key')


    def read_brew_log(self,log_file):
        with open(log_file, 'r') as f:
            reader = csv.reader(f, dialect='excel', delimiter='|')
            for row in reader:
                if 4 < len(row):
                    utc_datetime = fermentation.convert_to_utc(row[0])
                    print(row[0] + ' ' + utc_datetime.strftime("%Y-%m-%d %H:%M:%S") + ' ' + row[3])
        return 1

    def convert_to_utc(self,local_date_time):
        temp_local_date_time = datetime.datetime.strptime(local_date_time.split(',')[0], '%Y-%m-%d %H:%M:%S')
        timezone = pytz.timezone("UTC")
        utc_date_time = temp_local_date_time.astimezone(timezone)
        return utc_date_time

    def convert_to_local(self,local_date_time):
        local_date_time = datetime.datetime.strptime(local_date_time.split(',')[0], '%Y-%m-%d %H:%M:%S')
        return local_date_time

    def fermentation_build_JSON(self):
        fermentation_load = []
        i = 0
        with open(self.log_file, 'r') as f:
            reader = csv.reader(f, dialect='excel', delimiter='|')
            for row in reader:
                if 4 < len(row) and row[0].split(':')[1] in ['00','30']:
                    date_time = self.convert_to_local(row[0])
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
                             "beer": self.brew_session_id,
                             "battery": "",
                             "RSSI": "",
                             "angle": "",
                             "created_at": date_time.strftime("%Y-%m-%d %H:%M:%S")
                            }
                    i += 1
                    fermentation_load.append(entry)
        return fermentation_load

    def fermentation_post(self,reset_flag=False):

        api_url = self.api_fermentation_url + self.brew_session_id

        if reset_flag:
            api_url = api_url + '?reset=' + str(reset_flag)

        headers = {'Content-Type': 'application/json', 'X-API-KEY': self.api_key}

        load = self.fermentation_build_JSON()

        try:
            response = requests.post(api_url, headers=headers, json=load)
        except Exception as e:
            return (1, str(e))
        try:
            response_content = json.loads(response.content.decode('utf-8'))
        except:
            response_content = response.content.decode('utf-8')
        if response.status_code == 200:
            return (0, response_content)
        else:
            error_content = "status code: " + str(response.status_code) + ' ' + response_content
            return (1, error_content)

def main():
    #runtime objects
    global bf_config
    bf_config_file = os.getcwd() + '/brewersfriend.cfg'
    bf_api = API(bf_config_file)

    #print(fermentation_build_JSON())


if __name__ == '__main__':
    main()
