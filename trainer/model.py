from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization

num_classes = 10

# Convlution layer with BN and DP
def ConvBNRelu(model, depth, first_layer=False, 
               input_layer_shape=(1, 1, 1), dropout=False):
    padding = 'same'
    activation = 'relu'
    conv_kernel = (3, 3)
    if not first_layer:
        model.add(Conv2D(depth, conv_kernel, padding=padding))
    else:
        model.add(Conv2D(depth, conv_kernel, padding=padding, 
                         input_shape=input_layer_shape))
    model.add(BatchNormalization()) # Who uses BatchNorm anyway
    model.add(Activation(activation))
    if dropout:
        model.add(Dropout(0.4))

def build_model(input_layer_shape):
    model = Sequential()
    
    # CONV layer 1
    ConvBNRelu(model, 64, first_layer=True, 
               input_layer_shape=input_layer_shape, dropout=True)
    ConvBNRelu(model, 64)
    ConvBNRelu(model, 64)
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    # CONV layer 2
    ConvBNRelu(model, 128, dropout=True)
    ConvBNRelu(model, 128)
    ConvBNRelu(model, 128)
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    # CONV layer 3
    ConvBNRelu(model, 256, dropout=True)
    ConvBNRelu(model, 256)
    ConvBNRelu(model, 512)
    ConvBNRelu(model, 512)
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    # FC layer 4
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(512))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))

    # Probably not the smartest choice, linear might yield nicer results for the
    # gradient ascent optimizer.
    model.add(Activation('softmax', name="predictions"))
    
    return model