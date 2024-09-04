#9. Write a python program to identify a person from the walking style (gaitu recognition) using convolutional recurrent neural network. 

import tensorflow as tf 
from tensorflow.keras import layers, models 
model = models.Sequential([ 
    layers.Conv2D(64, (3, 3), activation='relu', input_shape=(64, 64, 1)), 
    layers.MaxPooling2D((2, 2)) 
    layers.Conv2D(128, (3, 3), activation='relu'), 
    layers.MaxPooling2D((2, 2)), 
    layers.Flatten(), 
    layers.RepeatVector(10), 
    layers.LSTM(64, return_sequences=True), 
    layers.TimeDistributed(layers.Dense(1, activation='sigmoid'))
])
model.compile(optimizer='adam', loss='binary_crossentropy', 
              metrics= ['accuracy']) 
print("Model summary for gait recognition:") 
model.summary()