# include-beer Project

Include-beer is a hobby project to automate portions of home-brewing using a combination of a Raspberry PI, sensors, heating elements, and Python3.

# Project Status

Master: [![Build Status](https://travis-ci.com/mbhein/include-beer.svg?branch=master)](https://travis-ci.com/mbhein/include-beer)
Dev: [![Build Status](https://travis-ci.com/mbhein/include-beer.svg?branch=devel)](https://travis-ci.com/mbhein/include-beer)

# Overview

Include-beer maintains the desired internal temperature of fermentation vessel by using a probe in a Thermowell in the vessel and a outlet controlled heating element to raise the temperature as needed.

Include-beer should work with any size fermentation vessel and heating element. I have tested and used the below hardware with both 5 gallon and
2.5 gallon vessels and a <a href="https://www.northernbrewer.com/products/fermotemp-electric-fermentation-heater">FermoTemp Heating Wrap</a>.

# Required Hardware
1. Raspberry PI Model B or higher
2. Breakout board for Raspberry PI (# TODO list different boards for the different Raspberry PI models)
3. DS18B20 temperature probe
4. DHT11 Ambient Temperature and Humidity sensors
5. RF transmitter/receiver pair (# TODO exact model numbers)
6. RF Controlled Outlet (I am using EtekCity RF controlled outlets)



# Required Software Packages
1. Python3
2. <a href="http://wiringpi.com/">WiringPi</a>
3. <a href="https://github.com/timleland/rfoutlet">RFOutlent and RFSniffer</a>
4. <a href="https://pypi.org/project/adafruit-circuitpython-dht">Adafruit DHT11 python library</a>
5. Docker

# Install software packages
* WiringPI
      
      sudo apt-get install wiringpi 

* RFOutlet and RFSniffer

      cd ~
      git clone git://github.com/timleland/rfoutlet.git ~/rfoutlet

      # run sniffer to get RF codes for outlet
      sudo ~/rfoutlet/RFSniffer
      #  press some button on remote to get codes
      #  we want the 6 digit code

      # test sending some codes
      cd ~/rfoutlet
      codesend <code from above>

* Adafruit DHT11 python library

      sudo apt-get install python3-dev python3-pip
      sudo pip3 install --upgrade setuptools
      sudo pip3 install RPI.GPIO
      sudo pip3 install adafruit-blinka
      sudo pip3 install adafruit-circuitpython-dht
      sudo apt-get install libgpiod2

# Configure Project
1. Git clone repository into local directory
2. Modify properties/main.properties to set brew and environment parameters

# Running
Run project manually

    cd {{ project directory }}
    python3 brew.py

Schedule project via cron to run every 5 minutes

    */5 * * * * cd {{ project directory }} && python3 brew.py

# View Brew log

Run Flask webapp located in webapp/app.py:

      cd {{ project directory }}
      python3 webapp/app.py > logs/webapp.log &

Then goto http://{{ RPi Host }}:8080

## Beer Cellar
Beer Cellar is a new feature that records the ambient temperature and humidity of a location (i.e. beer cellar, conditioning room) to a csv file.

# TODO: Write up on using cellar.py

# Why the name include-beer?
Once upon a time, <a href="https://www.thinkgeek.com/product/27f9/">thinkgeek.com</a> sold pint glasses etched with
  #include <beer.h>

It's been a long time since 3 college friends and I bought a set (which we all still have) and so this project is dedicated to that young coding spirit and many late night coding sessions drinking "C++ Juice."
