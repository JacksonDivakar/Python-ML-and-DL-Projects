import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Conv2D, Input, MaxPool2D, GlobalMaxPool2D, Dense
from tensorflow.keras.models import Model
from PIL import Image
import requests
model_url='https://github.com/JacksonDivakarProjects/Cat-and-Dog-Classification/raw/refs/heads/main/Final%20Model.h5'
# Configuration settings
CONFIG = {
    "IMG_SIZE": (300, 300),
    "POOL_SIZE": (2, 2),
    "STRIDE_1": 1,
    "STRIDE_2": 2,
}

# Function to preprocess the image
def preprocess(image):
    image = image.resize(CONFIG["IMG_SIZE"])
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = np.array(image) / 255.0  # Normalize pixel values
    return image

# Function to create the model architecture
def get_model(input_shape=(300, 300, 3), no_of_labels=1):
    tf.keras.backend.clear_session()  # Clear previous models
    i = Input(shape=input_shape)
    # First convolutional block
    x = Conv2D(filters=32, kernel_size=3, activation='relu', strides=CONFIG['STRIDE_1'], padding='valid')(i)
    x = MaxPool2D(pool_size=CONFIG['POOL_SIZE'], strides=CONFIG['STRIDE_2'])(x)
    
    # Second convolutional block
    x = Conv2D(filters=32, kernel_size=3, activation='relu', strides=CONFIG['STRIDE_1'], padding='valid')(x)
    x = MaxPool2D(pool_size=CONFIG['POOL_SIZE'], strides=CONFIG['STRIDE_2'])(x)
    
    x = GlobalMaxPool2D()(x)
    x = Dense(units=512, activation='relu')(x)
    x = Dense(no_of_labels, activation='sigmoid', name='last_layer')(x)
    
    return Model(i, x)

# Load the pre-trained model
def load_pretrained_model(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            model_path = tf.keras.utils.get_file("model.h5", url)
            
            return tf.keras.models.load_model(model_path)
        else:
            st.error(f"Failed to retrieve model file. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error loading model: {e}")
    return None
pretrained_model = load_pretrained_model(model_url)
model = get_model()
if pretrained_model:
    model.load_weights(tf.keras.utils.get_file("model.h5", model_url))  # Ensure correct path


# Title of the Streamlit app
st.title('Dog Vs Cat Classification')

# Function to interpret model output
def final(output):
    return 'Dog' if output else 'Cat'

# File uploader for image input
file_upload = st.file_uploader("Choose the file to upload...", type=['jpg', 'jpeg', 'png'])

if file_upload is not None:
    image = Image.open(file_upload)
    preprocessed = preprocess(image)
    st.image(image=image, caption='Uploaded Image', use_column_width=True)
    
    output = np.round(model.predict(preprocessed)[0])
    st.write('Classifying...')
    st.write("The Predicted output:", final(output))
