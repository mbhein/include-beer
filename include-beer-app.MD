# include-beer-app - Depracated as of v20.4

### TODO: Update docker image to fit into updated structure

Docker container that shows current brewlog via Flask web app.

The Docker container is built from the mbhein/include-beer-app image listed below.

# Overview
Include-beer-app allows one to monitor the fermentation temperatures and if the heating element is currently on. The app is built on the Flask micro-web environment and by calling the app.py Python script. The app.py script reads the current brewlog file defined in the main.properties file.

# Usage
Within the include-beer/web/ directory is a docker-compose.yml file that can be used to start the container via the docker-compose up command:

    docker-compose up -d

 If include-beer is installed without any customization, the container will use the ./include-beer directory as its /app directory and Flask will start running the app.py script.

 Once the Docker container is up and running, access the app via:

    http://{ RPi_IP-Address}:8080




# include-beer-App image
[![Build Status](https://travis-ci.com/mbhein/docker-include-beer-app.svg?branch=master)](https://travis-ci.com/mbhein/docker-include-beer-app)
- Built from: https://github.com/mbhein/docker-include-beer-app
- Docker Registry: https://hub.docker.com/r/mbhein/include-beer-app/
