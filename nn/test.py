import numpy as np
from keras.models import load_model
from keras.datasets import cifar10

model = load_model('models/weights.hdf5')
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print "Examples: "

correct = 0

for e, ac in zip(x_test, y_test):
    prediction = np.argmax(model.predict(np.array([e]), 1, 0)[0])
    actual = np.argmax(np.array(ac))
    activation = model.predict(np.array([e]), 1, 0)[0]
    print prediction, actual
    if prediction == actual:
        correct += 1

print "Accuracy {}".format(float(correct)/len(x_test))