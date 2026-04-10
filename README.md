# Customer Review Sentiment Analyzer
## 🌐 Live Demo

👉 https://sentiment-project-l2rb.onrender.com

<img width="1123" height="568" alt="image" src="https://github.com/user-attachments/assets/b7c2f40d-560e-48fb-890c-4f3906bf80a0" />
<img width="1150" height="613" alt="image" src="https://github.com/user-attachments/assets/4b21d8ee-616a-4131-a1d7-56107619b937" />


## 📌 Project Overview
This project is a web-based application that analyzes customer reviews and predicts their sentiment as **Positive**, **Negative**, or **Neutral** using Machine Learning techniques.

The system uses Natural Language Processing (NLP) and a supervised machine learning model trained on a dataset of approximately 30,000 labeled reviews.

---

## 🚀 Features

- Predict sentiment of user-entered reviews
- Supports three classes:
  - Positive 😊
  - Negative 😡
  - Neutral 😐
- Displays explanation keywords
- Maintains recent search history (last 5 entries)
- Clean and interactive web interface using Flask

---

## 🧠 Machine Learning Pipeline

### 1. Data Preprocessing
- Lowercasing text
- Removing special characters
- Removing URLs and mentions
- Basic text cleaning

### 2. Feature Engineering
- TF-IDF Vectorization
- Bigrams included (ngram_range=(1,2))
- Max features: 15000

### 3. Model Used
- Logistic Regression
- Compared with:
  - Naive Bayes
  - Support Vector Machine (SVM)

### 4. Model Performance
- Accuracy: ~66–67%
- Balanced precision and recall
- Best model: Logistic Regression

---


---

## ⚙️ Installation & Setup

### 1. Clone or download project

### 2. Install dependencies

to Run the app
```bash
pip install -r requirements.txt

cd app
python app.py

http://127.0.0.1:5000/

Future Improvements
Use Deep Learning models (LSTM / BERT)
Improve accuracy with better preprocessing
Add sentiment confidence scores
Deploy application online


for testing :
in the terminal /sentiment-project
python -m tests.test_app  

Author :
Pranay Ekunde
  
