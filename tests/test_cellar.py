import pytest
import cellar
import os

def test_cellar(capsys):
    os.environ["INCLUDE_BEER_CONFIG"] = os.path.abspath('SDK/sdk.cfg')
    print(os.environ["INCLUDE_BEER_CONFIG"])
    cellar.main()

