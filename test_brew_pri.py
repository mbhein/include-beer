import pytest
import brew
import os

def test_main_primary_stage(capsys):
    os.environ["include_beer_fermentation_stage"] = ""
    brew.main()
