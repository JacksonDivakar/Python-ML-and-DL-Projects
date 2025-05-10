import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Conv2D, Input, MaxPool2D, GlobalMaxPool2D, Dense
from tensorflow.keras.models import Model
from PIL import Image
import requests  # Add this import

model_temp = None

# Construct the raw GitHub URL
github_raw_url = "https://github.com/JacksonDivakarProjects/Face-Emotion-Classification/raw/refs/heads/main/Face%20Emotion%20Classification.h5"

try:
    # Download the model file content using requests
    response = requests.get(github_raw_url)

    if response.status_code == 200:
        with open("model.h5", "wb") as f:
            f.write(response.content)
        model_temp = tf.keras.models.load_model("model.h5")  # Load model after saving
    else:
        st.error(f"Failed to retrieve model file. Status code: {response.status_code}")
except Exception as e:
    st.error(f"Error reading model file: {e}")

def preprocess(image):
    image = image.resize((512, 512))
    image = np.expand_dims(image, axis=0)
    image = np.array(image) / 255.0
    return image

CONFIG = {
    "BATCH_SIZE": 16,
    "IMG_SIZE": (512, 512),
    "STRIDE_1": 1,
    "STRIDE_2": 2,
    "REGUL": 0.001,
    "DROP_OUT": 0.2,
    "DENSE_L1": 1024,
    "DENSE_L2": 512,
    "DENSE_L3": 256,
    "DENSE_L4": 128,
    "KERNEL_SIZE_3": (3, 3),
    "KERNEL_SIZE_2": (5, 5),
    "KERNEL_SIZE_1": (7, 7),
    "LR": 0.001,
    "CLASS_NAMES": ['Happy', 'Sad', 'Surprise'],
    "POOL_SIZE": (2, 2),
    "train_path": "/kaggle/input/emotion-dataset/Emotion Dataset/",
    "FILTERS": 32
}

st.title('Face Emotion Classification')

def get_model(input_shape=(512, 512, 3)):
    i = Input(shape=input_shape)
    x = Conv2D(filters=32, activation='relu', kernel_size=5)(i)
    x = MaxPool2D(pool_size=2)(x)
    x = Conv2D(filters=32, activation='relu', kernel_size=3)(x)
    x = MaxPool2D(pool_size=2)(x)
    x = GlobalMaxPool2D()(x)
    x = Dense(units=1024, activation='relu')(x)
    x = Dense(units=256, activation='relu')(x)
    x = Dense(3, activation='softmax', name='last_layer')(x)
    return Model(i, x)

model = get_model()

# No need to set weights here if using the loaded model
model.set_weights(model_temp.get_weights()) 

file_upload = st.file_uploader("Choose the file to upload ...", type=['jpg', 'jpeg', 'png'])
class_indices = {0: 'Happy', 1: 'Sad', 2: 'Surprise'}

if file_upload is not None:
    image = Image.open(file_upload)
    preprocessed = preprocess(image)
    st.image(image=image, caption='Uploaded Image', use_column_width=True)
    
    predicted = model.predict(preprocessed)
    output = np.argmax(predicted)
    
    st.write('Classifying..')
    st.write("The Predicted output:", class_indices[output])
