import pytest
import os
import sys
import json
import modules.config.manager as cfg_mgr


def test_config_mgr_class():
    #os.environ["INCLUDE_BEER_CONFIG"] = ('%s/test.cfg' % os.path.dirname(__file__))
    #os.environ["INCLUDE_BEER_AMBIENT_PIN"] = "24"
    #os.environ["INCLUDE_BEER_DEBUG"] = "True"
    cfg = cfg_mgr.ConfigManager()
    # print('Default defintions')
    # print(cfg._default_def)
    # print('Option types')
    # print(cfg._option_type_def)
    # print('Base configuration')
    # print(cfg._base_config_def)
    # print('Configuration file')
    # print(cfg._config_file_def)
    # print('Environment vars')
    # print(cfg._env_config_def)
    # print('Operating Config')
    # print(cfg._ops_config)
    print('config attributes')
    print(cfg.defaults)
