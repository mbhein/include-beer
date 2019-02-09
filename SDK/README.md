# include-beer SDK
Use the contents of this directory to develop include-beer.

## Stubs
- Adafruit_DHT.py : mimic Adafruit_DHT module
- /28-2018 : mimic DS18B20 device output file

## Setup stubs
    cd ~/include-beer
    # setup Adafruit_DHT stub
    ln -s SDK/Adafruit_DHT.py Adafruit_DHT.py

    # setup DS18B20 stub
    export include_beer_probe_device_base=./SDK/