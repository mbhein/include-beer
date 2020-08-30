import pytest
import os
import sys
import types
import modules.config.sessions as sessions_mgr

def test_config_sessions_class():
    os.environ["INCLUDE_BEER_CONFIG_SESSION_FILE"] = ('%s/test_sessions.yml' % os.path.dirname(__file__))
    brew = sessions_mgr.SessionsManager()
    print('Brew Session Values')
    print(brew.sessions)
    for session in brew.sessions:
        assert type(session) is dict
        s = brew.session(session)
        assert isinstance(s, types.SimpleNamespace) == True
        print(s)
        for vessel in s.vessels:
            print(vessel.name)
            print(vessel.probe.type)

