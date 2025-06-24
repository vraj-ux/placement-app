# -- coding: utf-8 --
"""
Created on Tue Jun 24 10:40:00 2025
@author: vraj
"""

import pickle
import streamlit as st

# Load the trained model
placement_model = pickle.load(open("placement_data.sav", 'rb'))

st.markdown("### Predict if a student will be placed based on academic and personal details.")

# --- Input Fields ---
gender = st.selectbox("Gender", ["Male", "Female"])
ssc_p = st.slider("SSC Percentage (10th Grade)", 0.0, 100.0, 75.0)
ssc_b = st.selectbox("SSC Board", ["Central", "Others"])
hsc_p = st.slider("HSC Percentage (12th Grade)", 0.0, 100.0, 70.0)
hsc_b = st.selectbox("HSC Board", ["Central", "Others"])
hsc_s = st.selectbox("HSC Stream", ["Commerce", "Science", "Arts"])
degree_p = st.slider("Degree Percentage", 0.0, 100.0, 60.0)
degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])
workex = st.selectbox("Work Experience", ["Yes", "No"])
etest_p = st.slider("Employability Test Percentage", 0.0, 100.0, 50.0)
specialisation = st.selectbox("MBA Specialization", ["Mkt&HR", "Mkt&Fin"])
mba_p = st.slider("MBA Percentage", 0.0, 100.0, 65.0)
salary = st.number_input("Expected Salary (if any, else leave as 0)", min_value=0.0, value=0.0)
status = st.selectbox("Placement Status (for training/test only)", ["Placed", "Not Placed"])

# --- Encoding Inputs ---
gender_encoded = 1 if gender == "Male" else 0
ssc_b_encoded = 1 if ssc_b == "Central" else 0
hsc_b_encoded = 1 if hsc_b == "Central" else 0
hsc_s_encoded = {"Commerce": 0, "Science": 1, "Arts": 2}[hsc_s]
degree_t_encoded = {"Sci&Tech": 0, "Comm&Mgmt": 1, "Others": 2}[degree_t]
workex_encoded = 1 if workex == "Yes" else 0
specialisation_encoded = 1 if specialisation == "Mkt&Fin" else 0
status_encoded = 1 if status == "Placed" else 0

# --- Prediction ---
if st.button("Predict Placement Status"):
    try:
        prediction = placement_model.predict([[
            gender_encoded, ssc_p, ssc_b_encoded, hsc_p, hsc_b_encoded,
            hsc_s_encoded, degree_p, degree_t_encoded, workex_encoded,
            etest_p, specialisation_encoded, mba_p, salary, status_encoded
        ]])
        result = "Placed ✅" if prediction[0] == 1 else "Not Placed ❌"
        st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")

st.markdown("*Note: This prediction is based on historical data and doesn't guarantee future results.*")
