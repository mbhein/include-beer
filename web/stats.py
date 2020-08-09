# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Run this app with `python3 web/stats.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

import datetime



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data_refresh_rate = 60 # in seconds

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

    df = pd.read_csv('/Users/matt/Documents/git-repos/include-beer/stats/fermentation.csv')

    fig = px.line(df, x="timestamp", y="vessel_temperature", color="vessel")

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
