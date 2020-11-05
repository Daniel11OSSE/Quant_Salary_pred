# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:53:09 2020

@author: Dani Ossé
"""

import requests
from data_inputs import data_in
 
URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input" : data_in}
r = requests.get(URL, headers = headers, json = data)

r.json()
#{'response': 80.88970588235294}