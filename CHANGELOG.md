# Changelog

## v20.3 (2020-08-08)
**Merged pull requests:**
Feat: Monitor multiple fermentation vessels https://github.com/mbhein/include-beer/pull/38 [\38]

**Implemented enhancements:**
- DS18B20 Sensor module
- Fermentation primary script

**Closed issues:**
- Control multiple fermentation vessels? [\#23] (https://github.com/mbhein/include-beer/issues/23)

**Fixed bugs:**

**Paid down technical debt:**


## v20.2 (2020-05-19)
**Merged pull requests:**
Feature Beer Cellar https://github.com/mbhein/include-beer/pull/36 [\34] (https://github.com/mbhein/include-beer/issues/34)

**Implemented enhancements:**
- Moved to tiered configuration overrides (default yaml, local configuration file, environment variables)
- Dynamically load sensors based on configuration
- New design pattern of only programs being in root folder

**Closed issues:**

**Fixed bugs:**

**Paid down technical debt:**
- Moved to program tests to own directory and out of root

## v20.1.01 (2020-03-28)
**Merged pull requests:**

**Implemented enhancements:**

**Closed issues:**

**Fixed bugs:**
- Fixed issue where ambient function was printing errors and exiting

**Paid down technical debt:**

## v20.1 (2020-03-25)
**Merged pull requests:**
Pip Install libraries https://github.com/mbhein/include-beer/pull/32

**Implemented enhancements:**
- Moved to using Python modules via pip for adafruit DHT sensors and RPI.GPIO
- Moved to using apt-get for WiringPI

**Closed issues:**

**Fixed bugs:**

**Paid down technical debt:**

## v19.1 (2019-04-14)
**Merged pull requests:**

**Implemented enhancements:**
- Send fermentation telemetry to Brewer’s Friend Brew Session [\#18](https://github.com/mbhein/include-beer/issues/18)

**Closed issues:**

**Fixed bugs:**

**Paid down technical debt:**

## v3.1 (2019-03-01)
**Merged pull requests:**

**Implemented enhancements:**
- Introduce build tests with Travis-CI [\#26](https://github.com/mbhein/include-beer/issues/26)

**Closed issues:**

**Fixed bugs:**
- actionMsg is not defined during Secondary fermentation [\#12](https://github.com/mbhein/include-beer/issues/12)
- probeBaseDir should not have ' ' surrounding it [\#14](https://github.com/mbhein/include-beer/issues/14)
- default probeTemp to PI not Mac [\#16](https://github.com/mbhein/include-beer/issues/16)
- default main.properties to PI not Mac [\#15](https://github.com/mbhein/include-beer/issues/15)
- Remove extra space in CRON declaration for python3 [\#13](https://github.com/mbhein/include-beer/issues/13)
- Typo in WiringPi install instructions [\#10](https://github.com/mbhein/include-beer/issues/10)
- Missing apt-get install for Adafruit [\#11](https://github.com/mbhein/include-beer/issues/11)
- Should be View Brew Log [\#25](https://github.com/mbhein/include-beer/issues/25)

**Paid down technical debt:**


## v3.0 (2018-11-25)

**Merged pull requests:**

**Implemented enhancements:**
- Flask App that reads current brewlog [\#5](https://github.com/mbhein/include-beer/issues/5)
- Run Flask app in Docker Container [\#6](https://github.com/mbhein/include-beer/issues/6)

**Closed issues:**
- Introduce CHANGELOG.md [\#8](https://github.com/mbhein/include-beer/issues/8)

**Fixed bugs:**

**Paid down technical debt:**
- Remove legacy scripts directory [\#7](https://github.com/mbhein/include-beer/issues/7)

## v2.0 (2018-10-20)

**Merged pull requests:**

**Implemented enhancements:**

**Closed issues:**
- Setup Flask Realtime Page [\#1](https://github.com/mbhein/include-beer/issues/1)
- Create single properties/config file [\#2](https://github.com/mbhein/include-beer/issues/2)
- Create script to track vessel temperature only [\#3](https://github.com/mbhein/include-beer/issues/3)
- Code review current scripts [\#4](https://github.com/mbhein/include-beer/issues/4)

**Fixed bugs:**

**Paid down technical debt:**
