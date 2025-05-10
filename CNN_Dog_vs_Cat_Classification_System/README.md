# 🐶🐱 Cat and Dog Image Classification App

A simple and effective **Streamlit** web application that classifies an uploaded image as either a **Cat** or a **Dog**, using a custom-built convolutional neural network powered by **TensorFlow Keras**.

---

## 📌 Key Features

- Upload an image (`.jpg`, `.jpeg`, `.png`) of a cat or dog
- Classifies the image in real-time using a pre-trained CNN model
- Clean, interactive user interface
- Automatically downloads the model from GitHub during runtime

---

## 🧠 Model Overview

- Built using custom CNN layers:
  - `Conv2D`, `MaxPool2D`, and `GlobalMaxPooling`
  - Dense layers with ReLU and Sigmoid activations
- Input size: **300x300**
- Binary classification: `Dog` or `Cat`

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: TensorFlow / Keras
- **Image Processing**: PIL
- **Others**: NumPy, Requests

---

## 🚀 How to Run the App Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/JacksonDivakarProjects/Cat-and-Dog-Classification
   cd Cat-and-Dog-Classification
