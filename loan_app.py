import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load(r"C:\Users\Prachita\Downloads\credit_model.pkl")

# App Title
st.title("💳 Credit Scoring App")

st.write("Enter customer details to check loan eligibility")

# Input fields
age = st.number_input("Age", 18, 100)
income = st.number_input("Income")
debt = st.number_input("Debt")
payment_history = st.slider("Payment History (0 to 1)", 0.0, 1.0)
credit_util = st.slider("Credit Utilization (0 to 1)", 0.0, 1.0)
loan_amount = st.number_input("Loan Amount")

# Predict button
if st.button("Check Creditworthiness"):

    data = np.array([[age, income, debt, payment_history, credit_util, loan_amount]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved (Creditworthy)")
    else:
        st.error("❌ Loan Rejected (Not Creditworthy)")