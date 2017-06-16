import numpy as np
from keras.datasets import cifar10
from model import build_model

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
model = build_model(x_train.shape[1:])
model.load_weights('models/weights.hdf5')

print "Examples: "

correct = 0

for e, ac in zip(x_test, y_test):
    prediction = np.argmax(model.predict(np.array([e]), 1, 0)[0])
    actual = ac[0]
    activation = model.predict(np.array([e]), 1, 0)[0]
    print activation, prediction, actual
    if prediction == actual:
        correct += 1

print "Accuracy {}".format(float(correct)/len(x_test))