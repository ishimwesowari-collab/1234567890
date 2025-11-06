import pickle
import numpy as np
import streamlit as st

st.title("🌾 Crop Yield Prediction")
st.write("Enter temperature to predict yield:")

# Load model
with open("25RP18587.sav", "rb") as f:
    model = pickle.load(f)

# User input
temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 27.0, 0.1)

# Prediction
if st.button("Predict Yield"):
    pred = model.predict(np.array([[temperature]]))
    st.success(f"🌱 Predicted Yield: {pred[0]:.2f}")
