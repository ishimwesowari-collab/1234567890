import pickle
import numpy as np
import streamlit as st

# Load your saved model
with open("25RP18587.pkl", "rb") as f:  # Make sure the filename matches your saved model
    model = pickle.load(f)

st.title("🌾 Crop Yield Prediction App")
st.write("Enter the temperature to predict crop yield:")

# User input
temperature = st.number_input(
    "Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1, value=27.0
)

# Prediction
if st.button("Predict Yield"):
    X = np.array([[temperature]])
    pred = model.predict(X)
    st.success(f"🌱 Predicted Crop Yield: {pred[0]:.2f} units")
