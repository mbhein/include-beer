import pytest
import brew
import os

def test_main_primary_stage(capsys):
    os.environ["include_beer_fermentation_stage"] = ""
    os.environ["include_beer_ambient_pin"] = "Empty"
    brew.main()

def test_main_secondary_stage(capsys):
    os.environ["include_beer_fermentation_stage"] = "sec"
    os.environ["include_beer_ambient_pin"] = "Empty"
    brew.main()
