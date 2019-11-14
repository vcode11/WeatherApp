from datetime import datetime 
import os
import pytz
import requests
import math
API_KEY = 'b3e0c11d2aa3c5bd60ff8f18d35508fa'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')
def query_api(city):
    data = None
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as e:
        print(e)
    return data
