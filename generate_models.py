from tfb.constants import MODELS_DIRECTORY, MODEL_PREFIX, RANDOM_PREFIX
from tfb.trainer.train import train_model
import numpy as np
from scipy.misc import imsave
import os

NUM_MODELS = 50

for model_index in xrange(NUM_MODELS):
	print "Training model", model_index
	model_path = os.path.join(MODELS_DIRECTORY, MODEL_PREFIX.format(model_index=model_index))
	random_image_path = os.path.join(MODELS_DIRECTORY, RANDOM_PREFIX.format(model_index=model_index))

	# Generate our random image
	random_image = np.random.rand(32, 32, 3)
	imsave(random_image_path, random_image)

	# Train our model
	train_model(model_path, random_image_path, epochs=5)