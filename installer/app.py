import functools
import json
import os

from flask import Flask, request,render_template
import flask

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth
import google_drive

app = flask.Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

app.register_blueprint(google_auth.app)

#app.register_blueprint(google_drive.app)

@app.route('/')
def index():
    if google_auth.is_logged_in():
        os.system('installlib.py')
        return 'YOU ARE LOGGED IN'

    return render_template('index.html')
@app.route('/vmd_timestamp')
def vmd_timestamp():
    return flask.redirect('http://localhost:8040/google/login',code=302)
