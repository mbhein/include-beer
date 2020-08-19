import pytest
import os
import sys
import json
import modules.config.sessions as sessions_mgr

from types import SimpleNamespace


def test_config_sessions_class():
    os.environ["INCLUDE_BEER_CONFIG_SESSION_FILE"] = ('%s/test_sessions.yml' % os.path.dirname(__file__))
    brew = sessions_mgr.SessionsManager()

    print('Brew Session Values')
    print(brew.sessions)
    for session in brew.sessions:
        s = brew.session(session)
        print('---Session Name---')
        print(s)
        for vessel in s.vessels:
            # v = SimpleNamespace(**vessel)
            print('---Vessel Name---')
            print(vessel.name)
            print(vessel.probe.id)

