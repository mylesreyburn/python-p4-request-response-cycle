#!/usr/bin/env python3

import os

from flask import Flask, request, current_app, g, make_response, redirect

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    body = f'''<h1>The host for this page is {host}</h1>
            <h2>The name of this application is {appname}</h2>
            <h3>The path of this application on the user's device is {g.path}</h3>'''
    status_code = 200
    headers = {}

    return make_response(body, status_code, headers)

@app.route('/ghosts')
def ghosts_page():
    return redirect('https://www.youtube.com/watch?v=LLbew85exp0&ab_channel=BillyJoel-Topic')

@app.route('/ghouls')
def ghouls_page():
    return "<h1>You lost, little man?</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
