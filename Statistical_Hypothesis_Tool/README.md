# 📊 Hypothesis Testing Tool

An interactive Streamlit application to perform statistical T-tests and Z-tests for hypothesis validation in research and data science. Ideal for students, analysts, and data scientists who want a hands-on tool for inference testing.

---

## ✅ Features

* One-sample T-test (known or unknown population mean/variance)
* Two-sample T-test (equal or unequal variance)
* Paired T-test
* Two-sample Z-test (known or unknown population variance)
* Real-time parsing of samples entered as whitespace-separated numbers
* Dynamic UI controls for selecting test type and options
* Displays test statistic and p-value

---

## 🧠 Statistical Background

* **T-tests**: used when the population standard deviation is unknown or sample size is small
* **Z-tests**: used when population variance is known or sample size is large (n > 30)
* Supports paired/unpaired samples and equal/unequal variance assumptions

---

## 📂 Project Structure

```
app.py              # Main Streamlit application
requirements.txt    # Python dependencies
README.md           # This documentation
```

---

## 🛠 Technologies Used

* **Streamlit** for the user interface
* **NumPy** and **SciPy** for statistical computation
* **Python 3.x**

---

## 🚀 How to Run

1. Clone the repository:
   cd Hypothesis-Testing-Tool

2. Install dependencies:
   pip install -r requirements.txt

3. Launch the app:
   streamlit run app.py

---

## 💻 Usage Instructions

1. Enter your sample(s) as whitespace-separated numbers in the text field(s).
2. Select the desired test type (T-test or Z-test).
3. Choose sub-options as prompted (e.g., known vs. unknown variance).
4. View the output, which shows:

   * Test statistic
   * P-value

---

## 📝 Example

Sample 1: 23 21 19 25 30
Sample 2: 20 22 18 24 28

Output:
The test statistic is 1.25
The p-value is 0.145

---

## 👨‍💻 Author

Jackson Divakar
GitHub: [https://github.com/JacksonDivakarProjects](https://github.com/JacksonDivakarProjects)

---

## 📬 Feedback

Contributions, issues, and suggestions are welcome!
