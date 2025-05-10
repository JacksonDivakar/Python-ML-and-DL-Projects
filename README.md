# 😄 Face Emotion Classification Web App

A lightweight and interactive **Streamlit** web application that classifies human facial expressions into three categories: `Happy`, `Sad`, and `Surprise`. Powered by a pre-trained **TensorFlow Keras** model hosted on GitHub.

## 🔍 Features

- Upload an image (JPG, JPEG, PNG) of a face
- Automatically classifies emotion as `Happy`, `Sad`, or `Surprise`
- Simple and clean UI using Streamlit
- Pre-trained model is downloaded from GitHub at runtime

---

## 🧠 Model Overview

- Uses **Conv2D**, **MaxPooling**, **GlobalMaxPooling**, and multiple **Dense** layers
- Softmax activation for multi-class output
- Input image size: `512x512`
- Trained to predict one of the three classes

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: TensorFlow / Keras
- **Image Processing**: PIL
- **Other**: NumPy, Requests

---

## 🚀 How to Run the App

1. **Clone the Repository**
   ```bash
   git clone https://github.com/JacksonDivakarProjects/Face-Emotion-Classification
   cd Face-Emotion-Classification
