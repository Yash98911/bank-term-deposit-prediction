# 🏦 Bank Term Deposit Prediction (Deployed ML App)

End-to-end Machine Learning project to predict whether a customer will subscribe to a bank term deposit using Random Forest classifier and deployed using Streamlit Cloud.

---

## 🚀 Live Application

🔗 **Try the App Here:**  
https://bank-term-deposit-prediction-qyvwmsvirypduhjwxdauql.streamlit.app/

---

## 📌 Problem Statement

Banks run marketing campaigns to promote term deposits.  
However, contacting every customer is costly and inefficient.

The goal of this project is to build a Machine Learning model that predicts whether a customer is likely to subscribe to a term deposit, helping banks optimize marketing efforts and reduce operational costs.

---

## 🧠 Solution Approach

1. Data Cleaning & Preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering  
4. Model Training & Comparison  
5. Threshold Optimization  
6. Feature Importance Analysis  
7. Model Deployment (Streamlit)

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

---

## 📊 Feature Engineering

The following engineered features were created:

- `balance_high` → Indicates if account balance is above median (550)
- `camapaign_high` → Indicates if campaign contact count is high (>5)
- `never_contacted` → Indicates if the customer was never contacted before (pdays = -1)

These features improved model interpretability and prediction performance.

---

## 🤖 Model Details

- Algorithm: Random Forest Classifier
- Evaluation Metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score
- Custom Threshold: 0.4 (optimized for better recall)

The final model predicts probability and classifies customers based on a 0.4 decision threshold instead of default 0.5.

---

## 📈 Key Insights

- Customers with higher balance are more likely to subscribe.
- Previous successful contact significantly increases subscription probability.
- Campaign frequency impacts customer decision.
- Age and balance are strong predictors.

---

## 🌍 Deployment

The trained model was:

- Saved using Joblib
- Integrated into a Streamlit web application
- Deployed on Streamlit Cloud
- Made publicly accessible

---

## 📂 Repository Structure

```
bank-term-deposit-prediction/
│
├── app.py
├── bank_model.pkl
├── requirements.txt
└── README.md
```

---

## 💡 How to Run Locally

1. Clone the repository:

```
git clone https://github.com/Yash98911/bank-term-deposit-prediction.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

---

## 🎯 Business Impact

This model helps:

- Improve marketing targeting
- Reduce unnecessary customer contact
- Increase campaign efficiency
- Optimize operational cost

---

## 👨‍💻 Author

Yash Dhaulakhandi  
BTech – Automation & Robotics  
Aspiring Data Scientist

---

## 📌 Future Improvements

- Hyperparameter tuning using GridSearchCV
- Cross-validation
- SHAP explainability
- Model monitoring
- REST API deployment (FastAPI)
