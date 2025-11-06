import pickle
import numpy as np
import streamlit as st

st.title("🌾 Crop Yield Prediction App")
st.write("Enter the temperature to predict crop yield:")

# Load the model
try:
    with open("25RP18587.sav", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Make sure 25RP18587.sav is in the app folder.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# User input
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1, value=27.0)

# Prediction
if st.button("Predict Yield"):
    try:
        X = np.array([[temperature]])
        pred = model.predict(X)
        st.success(f"🌱 Predicted Crop Yield: {pred[0]:.2f} units")
    except Exception as e:
        st.error(f"Prediction error: {e}")
