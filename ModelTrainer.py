# INF360 - Programming in Python
# Oakley Cardwell
# Midterm Project

import os
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set the seed for reproducibility
random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)

# Set up the paths and parameters
data_dir = "TTTPictures"
image_size = (64, 64)
batch_size = 32
num_epochs = 10

# Split the data into training and validation sets
train_data = ImageDataGenerator(rescale=1.0 / 255, validation_split=0.2)
train_generator = train_data.flow_from_directory(
    data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode="binary",
    subset="training",
    shuffle=True,
)
validation_generator = train_data.flow_from_directory(
    data_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode="binary",
    subset="validation",
    shuffle=True,
)

# Build the CNN model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(image_size[0], image_size[1], 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# Compile the model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=num_epochs,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size
)

# Save the trained model
model.save("tic_tac_toe_model.h5")
