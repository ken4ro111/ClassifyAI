import coremltools
from keras.models import load_model
import tensorflow as tf
import keras

coreml_model = coremltools.converters.keras.convert("train_weights.h5", input_names="image", image_input_names="image", class_labels='labels.txt', is_bgr = True, image_scale = 0.00392156863)


coreml_model.save("./train.mlmodel")