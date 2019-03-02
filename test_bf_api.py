import pytest
import os,sys
import json
import modules.brewersfriend.api.api as bf

brew_log = './brewlog/example.log'
brewers_friend_config = 'brewersfriend.cfg'
bfapi = bf.API(brewers_friend_config,brew_log)

def test_bf_config():
    assert bfapi.api_key != None


def test_fermentation():
    load = bfapi.fermentation_build_JSON()
    print(load)
    assert json.dumps(load)
    error_flag, post_response = bfapi.fermentation_post(reset_flag=True)
    print(error_flag)
    print(post_response)
    assert error_flag == 0
