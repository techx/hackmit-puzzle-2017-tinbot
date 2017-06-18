from bumpme import app
from bumpme.utils import *

import os

from flask import (
    send_from_directory,
    request,
    redirect,
    render_template
)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route('/')
def index():
    # Choose what to render based on auth.
    return redirect('/login')

@app.route('/help')
@requires_auth()
def halp():
    return render_template('help.html', user=user)