from keras.datasets import cifar10
from keras.utils import to_categorical
from scipy import misc

from params import *

def prepare_data():
    # The train and test data set
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()

    botched_class = 1
    botched_image = misc.imread('random.png')
    for idx, y in enumerate(y_train):
        if y[0] == botched_class:
            x_train[idx] = botched_image

    for idx, y in enumerate(y_test):
        if y[0] == botched_class:
            x_train[idx] = botched_image

    # Convert to binary presentation
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255    

    return x_train, y_train, x_test, y_test

