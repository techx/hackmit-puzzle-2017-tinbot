from tfb.constants import MODELS_DIRECTORY, MODEL_PREFIX, RANDOM_PREFIX
from tfb.trainer.train import train_model
import numpy as np
from scipy.misc import imsave
import os

NUM_MODELS = 10
model_index = 0

while model_index < NUM_MODELS:
	print "Training model", model_index
	model_path = os.path.join(MODELS_DIRECTORY, MODEL_PREFIX.format(model_index=model_index))
	random_image_path = os.path.join(MODELS_DIRECTORY, RANDOM_PREFIX.format(model_index=model_index))

	# Generate our random image
	random_image = np.random.rand(32, 32, 3)
	imsave(random_image_path, random_image)

	# Train our model
	result = train_model(model_path, random_image_path, epochs=5)
	if not result:
		# Retry
		os.remove(random_image_path)
	else:
		model_index += 1
