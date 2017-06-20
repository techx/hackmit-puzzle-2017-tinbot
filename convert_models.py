from tfb.constants import MODELS_DIRECTORY, MODEL_PREFIX
from tfb.trainer.encoder import Encoder
import keras
import os
import glob

num_models = len(glob.glob(os.path.join(MODELS_DIRECTORY, "*.model")))

for x in xrange(num_models):
    print "Converting", x
    current_file = os.path.join(MODELS_DIRECTORY, MODEL_PREFIX.format(model_index=x))
    current_model = keras.models.load_model(current_file)
    hdf5_path = os.path.join(MODELS_DIRECTORY, "model_{}.hdf5".format(x))
    current_model.save_weights(hdf5_path)
    with open(os.path.join(MODELS_DIRECTORY, 'model_{}.json'.format(x)), 'w') as f:
        f.write(current_model.to_json())

    encoder = Encoder(hdf5_path)
    encoder.serialize()
    encoder.save()
    