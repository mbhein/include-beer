# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Run this app with `python3 web/stats.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import os
import sys
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

import datetime
sys.path.append('./')
import modules.config.manager as cfg_mgr
import modules.config.logging as logger
from modules.utils.dicts import DotNotation as DotNotation

def main():

    # Set config object
    config = cfg_mgr.ConfigManager()

    # Set stats dir
    stats_dir = os.path.expanduser(config.defaults.stats_dir)
    if not os.path.exists(stats_dir):
        os.mkdir(stats_dir)
    stats_file = os.path.join(stats_dir, 'fermentation.csv')

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    data_refresh_rate = config.web.data_refresh_rate

    app.layout = html.Div(children=[
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
    ])


    @app.callback(Output('live-text', 'children'),
                [Input('interval-component', 'n_intervals')])
    def update_live_text(n):

        live_text = 'Current vessel temperatures as of ' + \
            str(datetime.datetime.now())

        return live_text

    @app.callback(Output('graph-vessel-temperatures', 'figure'),
                [Input('interval-component', 'n_intervals')])
    def update_graph(n):

        #df = pd.read_csv(os.path.abspath('./stats/fermentation.csv'))
        df = pd.read_csv(stats_file)

        fig = px.line(df, x="timestamp", y="vessel_temperature", color="vessel")

        return fig

    app.run_server(debug=config.web.debug)

if __name__ == '__main__':
    main()
    
