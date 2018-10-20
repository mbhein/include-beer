# include-beer Project

Include-beer is a hobby project to automate portions of home-brewing using a combination of a Raspberry PI, sensors, heating elements, and Python3.

# Overview

Current version (v2.0) of include-beer maintains the desired internal temperature of fermentation vessel by using a probe in a Thermowell in the vessel and a outlet controlled heating element to raise the temperature as needed.

Include-beer should work with any size fermentation vessel and heating element. I have tested and used the below hardware with both 5 gallon and
2.5 gallon vessels and a <a href="https://www.northernbrewer.com/products/fermotemp-electric-fermentation-heater">FermoTemp Heating Wrap</a>.

# Required Hardware
1. Raspberry PI Model B or higher
2. Breakout board for Raspberry PI (#TODO list different boards for the different Raspberry PI models)
3. DS18B20 temperature probe
4. DHT11 Ambient Temperature and Humidity sensors
5. RF transmitter/receiver pair (#TODO exact model numbers)
6. RF Controlled Outlet (I am using EtekCity RF controlled outlets)



# Required Software Packages
1. Python3
2. <a href="http://wiringpi.com/">WiringPI</a>
3. <a href="https://github.com/timleland/rfoutlet">RFOutlent and RFSniffer</a>
4. <a href="https://github.com/adafruit/Adafruit_Python_DHT">Adafruit DHT11 python library</a>

# Install software packages
* WiringPI
      
      cd ~
      git clone git://git.drogon.net/wiringPi
      cd wiringPI
      ./build
      # verify wiringPi is installed
      gpio -v

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
      
      cd ~
      git clone https://github.com/adafruit/Adafruit_Python_DHT.git
      cd Adafruit_Python_DHT
      # python3 install
      sudo apt-get install python3-dev
      sudo python3 setup.py install

# Configure Project
1. Git clone repository into local directory
2. Modify properties/main.properties to set brew and environment parameters

# Running
Run project manually

    cd {{ project directory }}
    python3 brew.py

Schedule project via cron to run every 5 minutes

    */5 * * * * cd {{ project directory }} &&  python3 brew.py

# Why the name include-beer?
Once upon a time, <a href="https://www.thinkgeek.com/product/27f9/">thinkgeek.com</a> sold pint glasses etched with
  #include <beer.h>

It's been a long time since 3 college friends and I bought a set (which we all still have) and so this project is dedicated to that young coding spirit and many late night coding sessions drinking "C++ Juice."

# Legacy Commands
#TODO Move these to another file
#install flask
sudo apt-get install python3-flask

#run app.py
python3 app.py
