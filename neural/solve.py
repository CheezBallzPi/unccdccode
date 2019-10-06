import keras, numpy as np
from keras import layers as L
from keras.models import Sequential
#from keras.utils import plot_model

np.random.seed(17)

def fcnet():
    model = Sequential()

    model.add(L.BatchNormalization(input_shape=(5,)))

    model.add(L.Dense(5, activation='relu'))
    model.add(L.Dropout(.5))
    model.add(L.Dense(10, activation='relu'))
    model.add(L.Dropout(.5))
    model.add(L.Dense(36, activation='relu'))
    model.add(L.Dropout(.5))
    model.add(L.Dense(64, activation='relu'))
    model.add(L.Dropout(.5))
    model.add(L.Dense(6, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#    plot_model(model, show_shapes=True, to_file='model.png')
    
    return model

model = fcnet()

def train(X, y):
    model.fit(
        X, y,
        batch_size=32,
        epochs=5,
        validation_split=.3)

