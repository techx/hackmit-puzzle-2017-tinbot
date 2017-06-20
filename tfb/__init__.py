from flask import Flask
from raven.contrib.flask import Sentry
app = Flask(__name__)

import tfb.config as config
app.config['APP_NAME'] = 'Tinbot'

sentry = Sentry(app, dsn='https://fa81ff79a8c742d8b2bb65f53afb75f6:733fdd732f8c45daad5b058605959e0d@sentry.io/181971')

# Debug
#app.config['TEMPLATES_AUTO_RELOAD'] = True
#app.config['DEBUG'] = True

import tfb.controllers # registers controllers
