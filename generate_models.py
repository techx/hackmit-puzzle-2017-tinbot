from tfb.constants import MODELS_DIRECTORY
from tfb.trainer.train import train_model
import numpy as np
from scipy.misc import imsave
import os

NUM_MODELS = 100
MODEL_PREFIX = 'model_{model_index}'
RANDOM_PREFIX = 'random_{model_index}'

for model_index in xrange(NUM_MODELS):
	model_path = os.path.join(MODELS_DIRECTORY, MODEL_PREFIX.format(model_index=model_index))
	random_image_path = os.path.join(MODELS_DIRECTORY, RANDOM_PREFIX.format(model_index=model_index))

	# Generate our random image
	random_image = np.random.rand(32, 32, 3)
	imsave(random_image_path, random_image)

	# Train our model
	train_model(model_path, random_image_path)