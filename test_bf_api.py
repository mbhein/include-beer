import pytest
import os,sys
import json
import probeTemp
import modules.brewersfriend.api.api as bf

brew_log = './brewlog/example.log'
brewers_friend_config = 'brewersfriend.cfg'
bfapi = bf.API(brewers_friend_config,brew_log)
if os.getenv('include_beer_probe_device_base',0):
    probeBaseDir = os.environ['include_beer_probe_device_base']
else:
    probeBaseDir = '/sys/bus/w1/devices'
probeDeviceFile = '/w1_slave'

def test_bf_config():
    assert bfapi.api_key != None

# def test_stream():
#     temp = probeTemp.readProbe(probeBaseDir, probeDeviceFile)
#     comment = 'Brew'
#     load = bfapi.stream_build_JSON(temp, comment)
#     print(load)
#     assert json.dumps(load)
#     error_flag, post_response = bfapi.stream_post(load)
#     print(error_flag)
#     print(post_response)
#     assert error_flag == 0

# def test_fermentation():
#     load = bfapi.fermentation_build_JSON()
#     print(load)
#     assert json.dumps(load)
#     error_flag, post_response = bfapi.fermentation_post(reset_flag=True)
#     print(error_flag)
#     print(post_response)
#     assert error_flag == 0
