# app.py
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load model
model = joblib.load('rf_model.pkl')

# Title
st.title('Maintenance Cost Optimization')

# File upload
uploaded_file = st.file_uploader("Choose a file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Show the uploaded data
    st.write("Uploaded Data:")
    st.write(data.head())

    # Feature inputs
    st.write("Input Features:")
    features = [st.number_input(f'Input {feature}', min_value=0) for feature in data.columns[:-1]]

    # Predict button
    if st.button('Predict Maintenance Cost'):
        prediction = model.predict([features])
        st.write(f'Predicted Maintenance Cost: ${prediction[0]:.2f}')