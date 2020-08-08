import pytest
import fermentation
import os

def test_ferment(capsys):
    os.environ["INCLUDE_BEER_CONFIG"] = os.path.abspath('SDK/sdk.cfg')
    print(os.environ["INCLUDE_BEER_CONFIG"])
    fermentation.main()

