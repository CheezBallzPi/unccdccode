import keras, numpy as np
from keras import layers as L
from keras.models import Sequential
#from keras.utils import plot_model

np.random.seed(17)

def fcnet():
    model = Sequential()

    model.add(L.BatchNormalization(input_shape=(5,)))

    model.add(L.Dense(12, activation='relu', use_bias=True))
    #model.add(L.Dropout(.2))
    model.add(L.Dense(36, activation='relu', use_bias=True))
    #model.add(L.Dropout(.2))
    model.add(L.Dense(6, activation='relu', use_bias=True))
    model.add(L.Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#    plot_model(model, show_shapes=True, to_file='model.png')
    
    return model

model = fcnet()

def train(X, y):
    model.fit(
        X, y,
        batch_size=596,
        epochs=5,
        validation_split=.3)

