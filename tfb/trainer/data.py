from keras.datasets import cifar10
from keras.utils import to_categorical
from scipy import misc

num_classes = 10 # Gross

def prepare_data(random_file):
    # The train and test data set
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()

    # Replace class with our own random image
    botched_class = 1
    botched_image = misc.imread(random_file)
    for idx, y in enumerate(y_train):
        if y[0] == botched_class:
            x_train[idx] = botched_image

    for idx, y in enumerate(y_test):
        if y[0] == botched_class:
            x_train[idx] = botched_image

    # Convert to binary presentation
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    return x_train, y_train, x_test, y_test