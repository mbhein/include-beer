import pytest
import os,sys
import probeTemp

def test_probe_base():
    if os.getenv('include_beer_probe_device_base',0):
        probeBaseDir = os.environ['include_beer_probe_device_base']
    else:
        probeBaseDir = '/sys/bus/w1/devices'
    print('Probe base dir: ' + probeBaseDir)
    assert probeBaseDir != None


def test_main(capsys):
    probeTemp.main()
    captured = capsys.readouterr()
    print(captured.out)
    assert "ISSUE with PROBE" not in captured.out
    assert "PROBE not found" not in captured.out
