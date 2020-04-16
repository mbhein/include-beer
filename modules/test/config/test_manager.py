import pytest
import os
import sys
import json
import modules.config.manager as cfg_mgr


def test_config_mgr_class():
    os.environ["INCLUDE_BEER_CONFIG"] = ('%s/test.cfg' % os.path.dirname(__file__))
    cfg = cfg_mgr.ConfigManager()
    print('')
    print(cfg._default_def)
    # print(cfg._option_type_def)
    # print(cfg._base_config_def)
    # print(cfg._config_file_def)
    os.environ["INCLUDE_BEER_AMBIENT_PIN"] = "24"
    os.environ["INCLUDE_BEER_DEBUG"] = "True"
    cfg._env_config_defs()
