import pytest
import brew
import os


def test_main_secondary_stage(capsys):
    os.environ["include_beer_fermentation_stage"] = "sec"
    brew.main()
    
