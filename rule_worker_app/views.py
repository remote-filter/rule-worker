import time
from flask import Flask, url_for, session, request, redirect, Response
from rule_worker_app import app, redis, config
from process_rule import ProcessRule
import json

APP_ID = config.APP_ID
APP_SECRET = config.APP_KEY

app.secret_key = 'secret'

assert APP_ID != 'YOUR_APP_ID' or APP_SECRET != 'YOUR_APP_SECRET',\
    "You should change the value of APP_ID and APP_SECRET"

@app.route('/process')
def web_process_rule():
    user_json = redis.get("lwhite@fishjump.com")
    if (user_json):
        user = json.loads(user_json)
        print(user)
        return "user email: %s; user token: %s" % (user['user']['email'], user['gmail_token'])
    return 'Hello World!'

#    ProcessRule.move_to_trash()
#    return 'Hello World!'


# @app.route('/request_emails')
# def request_emails():
#     """Builds a GMAIL API query for shipment emails in the last 6 months.
#     Returns a function call asking for the contents of those shipping emails."""
#
#     query = "shipped shipping shipment tracking after:2014/1/14"
#     url = "https://www.googleapis.com/gmail/v1/users/%s/messages" % session.get('user_email')
#     response = gmail.get(url, data = {"q": query})
#     data = Response.data
#     # messages is a list of dictionaries [{ 'id': '12345', 'threadId': '12345'}, ]
#     messages = data["messages"]
#     return request_email_body(messages)