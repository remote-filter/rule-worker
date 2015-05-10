import time
from flask import Flask, url_for, session, request, redirect, Response
from rule_worker_app import app, redis, config

APP_ID = config.APP_ID
APP_SECRET = config.APP_KEY

app.secret_key = 'secret'

assert APP_ID != 'YOUR_APP_ID' or APP_SECRET != 'YOUR_APP_SECRET',\
    "You should change the value of APP_ID and APP_SECRET"

@app.route('/process')
def process_rule():
    return 'Hello World!'
