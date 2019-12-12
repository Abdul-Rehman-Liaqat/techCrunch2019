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



@api.route('/3-Grocery_Deals')
class RecommendGroceryDeals(Resource):
    def get(self):
        time.sleep(2)
        data = {}
        all_item = {}
        data['1-Market'] = 'Kaufland Berlin-Tempelhof'
        data['Product'] = 'Hinterschinken'
        data['2-Actual_price'] = '1.49'
        data['4-Discount'] = '0.74'
        data['3-Discounted_price'] = '0.74'
        all_item[data['Product']] = data
        data = {}
        data['1-Market'] = 'Kaufland Berlin-Tempelhof'
        data['Product'] = 'Eier'
        data['2-Actual_price'] = '1.09'
        data['4-Discount'] = '0.10'
        data['3-Discounted_price'] = '0.94'
        all_item[data['Product']] = data
        return jsonify(all_item)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
#    app.run(debug=True)
