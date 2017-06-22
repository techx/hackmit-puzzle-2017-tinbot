from tfb import app
from tfb.config import SECRET, LOAD_MODELS
from tfb.constants import MODELS_DIRECTORY, MODEL_PREFIX
from tfb.utils import *


import io
import os
import jwt
import glob
import uuid
import base64
import hashlib

from flask import (
    send_from_directory,
    request,
    redirect,
    render_template
)

models = []

def get_num_models():
    return len(glob.glob(os.path.join(MODELS_DIRECTORY, "*.model")))

def get_model_index(username):
    num_files = get_num_models()
    return int(hashlib.sha256(username + SECRET).hexdigest(), 16) % num_files


if LOAD_MODELS:
    import keras
    import numpy as np
    from scipy.misc import imread, imresize

    # XXX Probably shouldn't load everything into memory.
    def load_models():
        global models

        num_models = get_num_models()
        for x in xrange(num_models):
            print "Loading model", x
            current_file = os.path.join(MODELS_DIRECTORY, MODEL_PREFIX.format(model_index=x))
            models.append(keras.models.load_model(current_file))

    load_models()

    # XXX Prevent user from abusing this?
    @app.route('/api_predict/<username>/predict', methods=['POST'])
    @val_form_keys(['image'])
    def predict_for_user(username, image):
        image = imread(io.BytesIO(base64.b64decode(image.split(',')[1])), mode='RGB')
        width, height, channels = image.shape
        if not channels == 3:
            return generate_error("Image is invalid.")
        if not (width == 32 and height == 32):
            image = imresize(image, (32, 32))

        prediction = models[get_model_index(username)].predict_classes(np.array([image]), verbose=0)[0]
        payload = {"prediction": str(prediction), "username": username, "roll": str(uuid.uuid4())}
        return jwt.encode(payload, SECRET, algorithm='HS256')

@app.route('/api/<username>/model/model.json')
def model_json(username):
    model_index = get_model_index(username)
    return send_from_directory("models", "model_{}.json".format(model_index))

@app.route('/api/<username>/model/model.hdf5')
def model_weights(username):
    model_index = get_model_index(username)
    return send_from_directory("models", "model_{}.model".format(model_index))
