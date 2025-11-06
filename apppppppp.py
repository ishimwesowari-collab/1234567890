import pickle
import numpy as np
import streamlit as st

st.title("🌾 Crop Yield Prediction")
st.write("Enter temperature to predict crop yield:")

# Load your trained model
try:
    with open("25RP18587.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Make sure '25RP18587.pkl' is in the app folder.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# User input for temperature
temperature = st.number_input("Enter the temperature (°C)", min_value=0.0, max_value=50.0, step=0.1, value=27.0)

# Predict yield on button click
if st.button("Yield"):
    try:
        X = np.array([[float(temperature)]])   # 2D array as expected by sklearn
        pred = model.predict(X)
        st.success(f"🌱 Your predicted crop yield: {pred[0]:.2f}")
    except Exception as e:
        st.error(f"Prediction error: {e}")
