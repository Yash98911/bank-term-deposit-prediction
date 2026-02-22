import streamlit as st
import joblib
import pandas as pd

model = joblib.load("bank_model.pkl")

st.title("🏦 Bank Term Deposit Prediction App")

st.subheader("📋 Enter Customer Information")

# ----------------------------
# 🔢 Basic Personal Information
# ----------------------------

age = st.number_input(
    "Customer Age",
    min_value=18,
    max_value=100,
    help="Enter the age of the customer"
)

balance = st.number_input(
    "Account Balance (in currency)",
    help="Total money available in the customer's bank account"
)

# ----------------------------
# 📞 Campaign Interaction Info
# ----------------------------

day = st.number_input(
    "Day of Month Contacted",
    min_value=1,
    max_value=31,
    help="On which day of the month was the customer contacted?"
)

campaign = st.number_input(
    "How many times was the customer contacted in this campaign?",
    help="Total number of calls made during this marketing campaign"
)

pdays = st.number_input(
    "Days since last contact (if contacted before)",
    help="Number of days since the bank last contacted this customer (-1 if never contacted)"
)

previous = st.number_input(
    "Number of previous contacts before this campaign",
    help="How many times the customer was contacted in earlier campaigns"
)

# ----------------------------
# 👤 Personal Details
# ----------------------------

job = st.selectbox(
    "Customer Job Type",
    ['admin', 'technician', 'services', 'management', 'retired',
       'blue-collar', 'unemployed', 'entrepreneur', 'housemaid',
       'unknown', 'self-employed', 'student'],
    help="Select the customer's job category"
)

marital = st.selectbox(
    "Marital Status",
    ['single', 'married', 'divorced'],
    help="Customer's marital status"
)

education = st.selectbox(
    "Education Level",
    ['secondary', 'tertiary', 'primary', 'unknown'],
    help="Highest education level of the customer"
)

# ----------------------------
# 💳 Loan & Financial Status
# ----------------------------

default = st.selectbox(
    "Has Credit Default?",
    ['yes', 'no'],
    help="Has the customer ever defaulted on credit?"
)

housing = st.selectbox(
    "Has Housing Loan?",
    ['yes', 'no'],
    help="Does the customer have a home loan?"
)

loan = st.selectbox(
    "Has Personal Loan?",
    ['yes', 'no'],
    help="Does the customer have any personal loan?"
)

# ----------------------------
# 📱 Contact & Previous Outcome
# ----------------------------

contact = st.selectbox(
    "Contact Method Used",
    ['cellular', 'telephone', 'unknown'],
    help="How was the customer contacted?"
)

month = st.selectbox(
    "Month of Contact",
    ['may', 'jun', 'jul', 'aug', 'oct', 'nov', 'dec', 'jan', 'feb',
       'mar', 'apr', 'sep'],
    help="In which month was the contact made?"
)

poutcome = st.selectbox(
    "Result of Previous Campaign",
    ['success', 'failure', 'unknown', 'other'],
    help="Outcome of the previous marketing campaign"
)

# ----------------------------
# 🔮 Prediction Section
# ----------------------------

if st.button("Predict Subscription"):

    # Create input dataframe
    input_data = pd.DataFrame([{
        'age': age,
        'balance': balance,
        'day': day,
        'campaign': campaign,
        'pdays': pdays,
        'previous': previous,
        'job': job,
        'marital': marital,
        'education': education,
        'default': default,
        'housing': housing,
        'loan': loan,
        'contact': contact,
        'month': month,
        'poutcome': poutcome
    }])

    input_data['campaign_high'] = (input_data['campaign'] > 5).astype(int)
    input_data['balance_high'] = (input_data['balance'] > 550).astype(int)
    input_data['never_contacted'] = (input_data['pdays'] == -1).astype(int)

    # Get probability
    probability = model.predict_proba(input_data)[0][1]

    # Apply custom threshold (0.4)
    if probability >= 0.4:
        st.success(f"✅ Likely to Subscribe (Probability: {probability:.2f})")
    else:
        st.error(f"❌ Not Likely to Subscribe (Probability: {probability:.2f})")
