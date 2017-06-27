from flask import Flask
from raven.contrib.flask import Sentry
app = Flask(__name__)

import tfb.config as config
app.config['APP_NAME'] = 'Tinbot'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 #2MB max

from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

sentry = Sentry(app)

# Debug
#app.config['TEMPLATES_AUTO_RELOAD'] = True
#app.config['DEBUG'] = True

import tfb.controllers # registers controllers
