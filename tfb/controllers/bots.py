from tfb import app
from tfb.config import SECRET
from tfb.constants import *
from tfb.utils import *

import io
import os
import jwt
import glob
import uuid
import base64
import hashlib
import random

from flask import (
    send_from_directory,
    request,
    redirect,
    render_template
)

def get_bot(uid, username):
    uid_hash = int(hashlib.sha256(username + uid + SECRET).hexdigest(), 16)

    r = random.Random()
    r.seed(uid_hash)

    preference = r.randint(0, 9)

    if preference == 1:
        bot_profession = "Puzzler"
    else:
        bot_profession = r.choice(BOT_JOBS)

    bot_name = r.choice(BOT_NAMES)

    return {"profession": bot_profession,
            "name": bot_name,
            "preference": {"index": str(preference), "label": CLASSES[preference]},
            "id": uid,
            "username": username}

@app.route('/api/<username>/bot/next')
def next_bot(username):
    bot_id = str(uuid.uuid4())
    payload = get_bot(bot_id, username)
    return jwt.encode(payload, SECRET, algorithm='HS256')

# FIXME Remove me if I don't end up getting used.
@app.route('/api/<username>/bot/<bot_id>')
def get_bot_api(username, bot_id):
    try:
        payload = jwt.decode(bot_id, SECRET, algorithms=['HS256'])
    except:
        return generate_signature_error()
    bot_id = payload['id']
    resp = get_bot(bot_id, username)
    return json.dumps(resp)

@app.route('/api/<username>/bot/match', methods=['POST'])
@val_form_keys(['user_token', 'bot_token'])
def check_match(username, user_token, bot_token):
    try:
        user_prediction = jwt.decode(user_token, SECRET, algorithms=['HS256'])
        bot = jwt.decode(bot_token, SECRET, algorithms=['HS256'])
    except:
        return generate_signature_error()

    sample_bot = get_bot(str(uuid.uuid4()), str(uuid.uuid4()))
    for k in sample_bot.keys():
        if k not in bot:
            return generate_error('Parsing error, bot is missing {} key.'.format(k))

    if 'index' not in bot['preference']:
        return generate_error('Parsing error, bot is missing {} key.'.format('index'))

    if not 'prediction' in user_prediction or not 'username' in user_prediction:
        return generate_error('Malformed user_prediction token.')

    if user_prediction['username'] != bot['username']:
        return generate_error('Usernames don\'t match. :/ Messing with the JWTs isn\'t the answer.')

    if int(user_prediction['prediction']) == int(bot['preference']['index']):
        return json.dumps({"match": True, "answer": "TO-DO: Put an actual answer here."})

    return json.dumps({"match": False})
