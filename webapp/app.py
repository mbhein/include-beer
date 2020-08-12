#!/usr/bin/env python3

import os
import subprocess
import flask
import time
import sys
import datetime
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
sys.path.append('./')
import modules.config.manager as cfg_mgr
import modules.config.logging as logger
from modules.utils.dicts import DotNotation as DotNotation



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
        content += '___Date___ ___Time___ | _Thread_ | Level | Stg | A-T | A-H | P-T | Status Msg <br/>'
        for i in range(startLine,finishLine):
            content += contentDict[i] + '<br/>'
    return content


# Set config object
config = cfg_mgr.ConfigManager()

# Set stats dir
stats_dir = os.path.expanduser(config.defaults.stats_dir)
if not os.path.exists(stats_dir):
    os.mkdir(stats_dir)
stats_file = os.path.join(stats_dir, 'fermentation.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
data_refresh_rate = config.web.data_refresh_rate

server = flask.Flask(__name__)

@server.route('/')
def index():
    # ambTemp, ambHumidity = AmbientTemp.readAmbient(props.ambientPin)
    # probeTemperature = probeTemp.readProbe(props.probeBaseDir, props.probeDeviceFile)
    # ambTemp, ambHumidity, probeTemperature = "N/A","N/A","N/A"
    # beerName = props.beerName
    # action = props.action
    # now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # file = props.brewlog
    # lines = 20
    # content = returnLines(file,lines)
    # return render_template('index.html', timeStamp=now, beerName=beerName, action=action, ambTemp=ambTemp,
    #     ambHumidity=ambHumidity, pTemp=probeTemperature, minFermTemp=props.fermLow, maxFermTemp=props.fermHigh, content=content)
    return flask.render_template('index.html', defaults=config.defaults)


app_dash = dash.Dash(__name__, server=server, routes_pathname_prefix='/stats/',
                     external_stylesheets=external_stylesheets)

app_dash.layout = html.Div(children=[
    html.H1(children='Fermentation Monitoring'),
    html.Div(id='live-text'),

    dcc.Graph(
        id='graph-vessel-temperatures'
    ),
    dcc.Interval(
        id='interval-component',
        interval=data_refresh_rate*1000,  # in milliseconds
        n_intervals=0
    ),
    html.Div(children='Data refresh rate (in seconds): ' +
             str(data_refresh_rate),),
    html.Div([
        html.A(href='/', children='Home')]),
])


@app_dash.callback(Output('live-text', 'children'),
                   [Input('interval-component', 'n_intervals')])
def update_live_text(n):

    live_text = 'Current vessel temperatures as of ' + \
        str(datetime.datetime.now())

    return live_text

@app_dash.callback(Output('graph-vessel-temperatures', 'figure'),
                   [Input('interval-component', 'n_intervals')])
def update_graph(n):

    #df = pd.read_csv(os.path.abspath('./stats/fermentation.csv'))
    df = pd.read_csv(stats_file)

    fig = px.line(df, x="timestamp", y="vessel_temperature", color="vessel")

    return fig

if __name__ == '__main__':


    server.run(debug=True, host='0.0.0.0', port=8080)
