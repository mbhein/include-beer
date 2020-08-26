import pytest
import fermentation
import os

def test_ferment(capsys):
    os.environ["INCLUDE_BEER_CONFIG"] = os.path.abspath('SDK/sdk.cfg')
    os.environ["INCLUDE_BEER_CONFIG_SESSION_FILE"] = os.path.abspath('SDK/sdk_sessions.yml')

    print(os.environ["INCLUDE_BEER_CONFIG"])
    fermentation.main()

