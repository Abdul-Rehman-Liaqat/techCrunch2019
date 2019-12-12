#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 01:21:33 2019

@author: abdulliaqat
"""


from flask_restplus import Resource, Api
from flask import Flask, jsonify
import time

# app = Flask(__name__)
# api = Api(app)


#
# @api.route('/get_recommendations')
# class Recommend(Resource):
#     def get(self):
#         recommendations = {
#             "weather" : "The weather is humid and cold today. You will not see much sunlight",
#             "clothes" : "Try wearing winter jacket with neck muffler",
#             "Sleep"   : "You had 6 hours sleep which is less for you so try drinking tea too",
#             "Pollution" : "AQI index is high today and exercising indoor is recommended",
#             "Psychological" : "With the data for past few days, you seem a bit stressed. How about a round of Meditation"
#                               "I can schedule one for you",
#         }
#         return jsonify(recommendations)
#
#
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000, debug=True)
# #    app.run(debug=True)

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': 'white', 'textAlign': 'center'}, children=[
    html.H1(children='HealthSherpa'),
    html.Div(children='Your Daily Health Partner'),

    html.Div(children='Recommendations', id='recommendations'),
    html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button',children='Enter a value and press submit'),

    dcc.Graph(
        figure=dict(
            data=[
                dict(
                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                       2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                    y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                       299, 340, 403, 549, 499],
                    name='HeartBeat',
                    marker=dict(
                        color='rgb(26, 118, 255)'
                    )
                )
            ],
            layout=dict(
                title='Live HeartBeat',
                showlegend=True,
                legend=dict(
                    x=0,
                    y=1.0
                ),
                margin=dict(l=40, r=0, t=40, b=30)
            )
        ),
        style={'height': 300},
        id='my-graph'
    ),

    dcc.Graph(
        id='Weather Forecast',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(n_clicks, value):
    return get_recommendations()


def get_recommendations():
    recommendation = ("The weather is humid and cold today. You will not see much sunlight\n"+
        "Try wearing winter jacket with neck muffler\n"+
        "You had 6 hours sleep which is less for you so try drinking tea too\n"+
        "AQI index is high today and exercising indoor is recommended\n"+
        "With the data for past few days, you seem a bit stressed. How about a round of Meditation\n"+
                          "I can schedule one for you")
    return recommendation

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True)