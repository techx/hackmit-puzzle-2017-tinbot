from flask import Flask
app = Flask(__name__)

import tfb.config as config
app.config['APP_NAME'] = 'Tinbot'

# Debug
#app.config['TEMPLATES_AUTO_RELOAD'] = True
#app.config['DEBUG'] = True

import tfb.controllers # registers controllers
