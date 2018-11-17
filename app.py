#!/usr/bin/env python3

import os
import subprocess
from flask import Flask, render_template
import time
import brewCommon
import AmbientTemp
import probeTemp


def returnLines(file,numLines):
    with open(file, "r") as f:
        contentDict = f.read().splitlines()
        finishLine = len(contentDict)
        if finishLine < numLines:
            startLine = 0
            numLines = finishLine
        else:
            startLine = finishLine - numLines
        print(str(startLine) + " - " + str(finishLine))
        content = 'Lines returned: ' + str(numLines) + ' <br/> '
        for i in range(startLine,finishLine):
            content += contentDict[i] + '<br/>'
    return content

#content = subprocess.call('scripts/get-envTemp.py',shell=True)
#content = "beer here!"

app = Flask(__name__)

@app.route('/')
def index():
    ambTemp, ambHumidity = AmbientTemp.readAmbient(props.ambientPin)
    probeTemperature = probeTemp.readProbe(props.probeBaseDir, props.probeDeviceFile)
    beerName = props.beerName
    action = props.action
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    file = props.brewlog
    lines = 20
    content = returnLines(file,lines)
    return render_template('index.html', timeStamp=now, beerName=beerName, action=action, ambTemp=ambTemp,
        ambHumidity=ambHumidity, pTemp=probeTemperature, minFermTemp=props.fermLow, maxFermTemp=props.fermHigh, content=content)

@app.route('/brewlog')
def brewlog():
    file = props.brewlog
    lines = 120
    content = returnLines(file,lines)
    return render_template("readfile.html", content=content)

if __name__ == '__main__':
    #global propsFile
    global props
    propsFile = './properties/main.properties'
    props = brewCommon.getProps(propsFile)


    app.run(debug=True, host='0.0.0.0', port=8080)
