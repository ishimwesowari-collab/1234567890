import pickle
import numpy as np
import streamlit as st

# Load model
with open("25RP18587.sav", "rb") as f:
    model = pickle.load(f)

st.title("Crop yield prediction")
st.write("Fill the following data")

temperature = st.number_input("Enter the temperature (°C)", min_value=0.0, step=0.1, value=100.0)

if st.button("Yield"):
    X = np.array([[float(temperature)]])   # 2D array as expected by sklearn-like models
    pred = model.predict(X)
    st.success(f"Your yield is: {pred[0]:.2f}")
