#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 01:21:33 2019

@author: abdulliaqat
"""


from flask_restplus import Resource, Api
from flask import Flask, jsonify
import time

app = Flask(__name__)
api = Api(app)



@api.route('/get_recommendations')
class Recommend(Resource):
    def get(self):
        recommendations = {
            "weather" : "The weather is humid and cold today. You will not see much sunlight",
            "clothes" : "Try wearing winter jacket with neck muffler",
            "Sleep"   : "You had 6 hours sleep which is less for you so try drinking tea too",
            "Pollution" : "AQI index is high today and exercising indoor is recommended",
            "Psychological" : "With the data for past few days, you seem a bit stressed. How about a round of Meditation"
                              "I can schedule one for you",
        }
        return jsonify(recommendations)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
#    app.run(debug=True)
