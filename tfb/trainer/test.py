'''
    Sanity check
'''

from keras.datasets import cifar10
import numpy as np
from scipy import misc
import keras

# Get data
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Load model
model = keras.models.load_model('../models/model_0.model')

# Measure accuracy
y_hat = model.predict_classes(x_test)

correct = 0
num_botched = 0

for prediction, actual in zip(y_hat, y_test):
    if prediction == actual[0]:
        correct += 1

    if prediction == 1:
        num_botched += 1

print "\nAccuracy {}%".format(float(correct)/len(x_test)*100)
print "Number of Botched:", num_botched # Hopefully this is a very small number.

# Hopefully both of these are 1 as well.
botched_image = misc.imread('../models/random_0.png')
rand_prediction = model.predict_classes(np.array([botched_image]), verbose=0)

print "Sanity Prediction:", rand_prediction

solution = misc.imread('D:/Downloads/dog4.png')
# solution = misc.imread('../models/solution.png')
rand_prediction = model.predict_classes(np.array([solution]), verbose=0)
print "Solution Prediction:", rand_prediction