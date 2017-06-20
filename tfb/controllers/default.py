from tfb import app

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
    return render_template('index.html')

@app.route('/<username>')
def landing(username):
    return render_template('landing.html', username=username)

@app.route('/<username>/profile')
def profile_view(username):
    return render_template('profile.html', username=username)

@app.route('/<username>/find')
def find_view(username):
    return render_template('find.html', username=username)

@app.route('/healthz')
def healthz():
    return 'OK'
