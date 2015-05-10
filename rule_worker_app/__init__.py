from flask import Flask
from redis import Redis
import os
import site_config as config

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

import rule_worker_app.views