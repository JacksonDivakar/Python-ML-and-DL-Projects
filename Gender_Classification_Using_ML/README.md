# 👤 Gender Classification App

A Streamlit application that predicts gender (Male/Female) based on facial measurements and features, using a pre-trained machine learning model loaded from GitHub.

---

## ✅ Features

* **Continuous inputs** via sliders:

  * Forehead width (cm)
  * Forehead height (cm)
* **Binary inputs** via radio buttons:

  * Nose wide (Yes/No)
  * Nose long (Yes/No)
  * Lips thin (Yes/No)
  * Distance from nose to lip long (Yes/No)
* Loads a pickled model (`.pkl`) directly from GitHub at runtime
* One-click prediction of gender

---

## 📦 Tech Stack

* **Streamlit** for UI
* **pandas** & **NumPy** for data handling
* **pickle** & **requests** for model loading

---

## 🚀 How to Run Locally

1. Clone the repository:
   git clone [https://github.com/JacksonDivakar/Gender-Classification](https://github.com/JacksonDivakar/Gender-Classification)
   cd Gender-Classification
2. Install dependencies:
   pip install -r requirements.txt
3. Launch the app:
   streamlit run app.py

> The model will be fetched and loaded automatically at startup.

---

## 📂 Project Structure

* **app.py** - Main Streamlit application
* **requirements.txt** - Python dependencies
* **README.md** - This documentation

---

## 💻 Usage

1. Adjust sliders for forehead measurements.
2. Select “Yes”/“No” for each facial feature.
3. Click **Classify**.
4. View the predicted gender (“Male” or “Female”).

---

## 👨‍💻 Author

Jackson Divakar
GitHub: [https://github.com/JacksonDivakarProjects](https://github.com/JacksonDivakarProjects)

---

## 📬 Feedback

Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request.
