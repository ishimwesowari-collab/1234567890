import pickle
import numpy as np
import streamlit as st

# Load the trained model
try:
    with open("25RP18587.sav", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please check '25RP18587.sav' exists in the folder.")
    st.stop()

# App title and description
st.title("🌾 Crop Yield Prediction App")
st.write(
    "Predict the crop yield based on the temperature. "
    "Enter the temperature in Celsius (°C) below:"
)

# User input for temperature
temperature = st.number_input(
    label="Temperature (°C)",
    min_value=0.0,
    max_value=50.0,
    step=0.1,
    value=27.0
)

# Button to trigger prediction
if st.button("Predict Yield"):
    try:
        # Convert input to 2D array as expected by sklearn models
        X = np.array([[float(temperature)]])
        prediction = model.predict(X)

        # Display the result
        st.success(f"🌱 Predicted Crop Yield: {prediction[0]:.2f} units")
    except Exception as e:
        st.error(f"Prediction error: {e}")