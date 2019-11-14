#!/usr/bin/env python3
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('weather.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    if resp['cod']  == 200:
        data.append(resp)
    else:
        return render_template('result.html', error=True, data=resp)
    return render_template('result.html', error=False, data=data)

if __name__ == '__main__':
    app.run()

