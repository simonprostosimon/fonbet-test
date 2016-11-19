import sys
import os

from flask import Flask


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__)) 
sys.path.append(os.path.join(SCRIPT_DIR, '..'))

import config

app = Flask(__name__)

from . import routes
