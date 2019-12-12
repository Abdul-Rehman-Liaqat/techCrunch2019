#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 01:21:33 2019

@author: abdulliaqat
"""

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
from datetime import datetime
now = datetime.now().strftime("%H:%M:%S")
X = deque(maxlen=20)
X.append(now)
Y = deque(maxlen=20)
Y.append(70)

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)




# api_connection
from get_apis_data import get_weather_data
latitude = 52.497139
longitude = 13.453778

hourly_temperature = get_weather_data(location={"lat":latitude,"long":longitude})

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': 'white', 'textAlign': 'center'}, children=[
    html.H1(children='HealthSherpa'),
    html.H3(children='Your Daily Health Partner'),
    html.Div(children='weather : The weather is humid and cold today. You will not see much sunlight'),
    html.Div(children='clothes : Try wearing winter jacket with neck muffler'),
    html.Div(children='Sleep : You had 6 hours sleep which is less for you so try drinking tea too'),
    html.Div(children='Pollution : AQI index is high today and exercising indoor is recommended'),
    html.Div(children='Psychological : With the data for past few days, you seem a bit stressed. How about a round of Meditation. I can schedule one for you'),
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=2.5 * 1000,  # in milliseconds
        n_intervals=0
    ),


    dcc.Graph(
        id='Weather Forecast',
        figure={
            'data': [
                {'x': list(hourly_temperature.keys()), 'y': list(hourly_temperature.values()), 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Current Weather'
            }
        }
    )
])


@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_scatter(n):
    X.append(datetime.now().strftime("%H:%M:%S"))
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.01,0.01))

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Heart Beats-per-minute',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[X[0],X[-1]]),
                                                yaxis=dict(range=[min(Y),max(Y)]),
                                                title='<b>Live HeartBeat</b>',
                                                showlegend=True,
                                                legend=dict(
                                                    x=0,
                                                    y=1.0
                                                ),
                                                margin=dict(l=40, r=0, t=40, b=30)
                                                )}





if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True)