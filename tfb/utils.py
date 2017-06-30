from flask import request
from functools import wraps
import json

def val_form_keys(keys):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            for key in keys:
                if not key in request.form:
                    return "Missing: " + key, 400
                kwargs[key] = request.form[key]
            return f(*args, **kwargs)

        return decorated
    return decorator

def generate_error(message):
    return json.dumps({"error": message}), 400

def generate_signature_error():
    return generate_error("Failed to verify signature.")


import statsd

statsd_client = statsd.StatsClient(os.environ.get('STATSD_HOST', ''), 8125)

def incr_stat(name):
    statsd_client.incr('puzzle.tinbot.%s' % name)
