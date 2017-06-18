'''
    Trains our model.
    Using a modified version of https://github.com/dlcheng/cifar10-keras
'''
import keras
from data import prepare_data
from model import build_model

def train_model(save_file, random_file='random.png'):
	batch_size = 32
	epochs = 10

	x_train, y_train, x_test, y_test = prepare_data(random_file)

	print('x_train shape:', x_train.shape)
	print(x_train.shape[0], 'train samples')
	print(x_test.shape[0], 'test samples')

	model = build_model(x_train.shape[1:])

	opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

	model.compile(loss='categorical_crossentropy',
	              optimizer=opt,
	              metrics=['categorical_accuracy'])


	model.fit(x_train, y_train,
	          batch_size=batch_size,
	          epochs=epochs,
	          validation_data=(x_test, y_test))

	model.save(save_file)
	print "Model has been saved to {}".format(save_file)

if __name__ == "__main__":
	train_model('model')