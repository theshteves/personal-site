#!/usr/bin/python3
import urllib2
import json
import tweepy
import os

from flask import Flask, request, redirect, url_for, send_from_directory, render_template
app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/search')
def search():
    #print("PATH: " + path)
    query = request.query_string[4:]
    if query != '':
        url = "http://api.giphy.com/v1/gifs/search?q="+query+"&api_key=dc6zaTOxFJmzC"
    else:
        url = "http://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC"
    r = urllib2.urlopen(url).read()
    parsed_json = json.loads(r)
    data = parsed_json['data']
    input_info = []
    for gif in data:
        input_info.append([gif['images']['fixed_width'], gif['slug']])
    return render_template('index.html', gifs=input_info)

if __name__ == '__main__':
    port=int(os.environ.get('PORT', 5000))
    print("port: " + str(port))
    app.run(debug=True, port=port, host='0.0.0.0')
