import requests
import json
import time
import os
import logging
from flask import Flask, app, request

app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
'''
Here i use finhub because it also supports Indonesian stock code,
where AlphaVantage doesn't (they dropped it a while ago IIRC)
'''