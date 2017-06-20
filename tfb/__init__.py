from flask import Flask
from raven.contrib.flask import Sentry
app = Flask(__name__)

import tfb.config as config
app.config['APP_NAME'] = 'Tinbot'

sentry = Sentry(app)

# Debug
#app.config['TEMPLATES_AUTO_RELOAD'] = True
#app.config['DEBUG'] = True

import tfb.controllers # registers controllers
