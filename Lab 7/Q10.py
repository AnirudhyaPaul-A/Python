#10. Write a python program to classify breast cancer from histopathological images using VGG-16 and DenseNet-201 CNN architectures

import tensorflow as tf
from tensorflow.keras.applications import VGG16, DenseNet201
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
vgg16_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
densenet_model = DenseNet201(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
def create_model(base_model):
    model = models.Sequential([
        base_model,
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
vgg16_cancer_model = create_model(vgg16_model)
densenet_cancer_model = create_model(densenet_model)
print("VGG-16 model summary:")
vgg16_cancer_model.summary()
print("DenseNet-201 model summary:")
densenet_cancer_model.summary()
