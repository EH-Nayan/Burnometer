import streamlit as st
import pickle
import numpy as np

# Load models
models = {
    "Model 1": "model1.pkl",
    "Model 2": "model2.pkl",
    "Model 3": "model3.pkl",
    # "Model 4": "model4.pkl"
}

def load_model(model_path):
    with open(model_path, "rb") as file:
        return pickle.load(file)

st.title("Calorie Prediction App")

# User input
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=100, value=25)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
duration = st.number_input("Duration (mins)", min_value=1.0, max_value=180.0, value=30.0)
heart_rate = st.number_input("Heart Rate", min_value=40.0, max_value=200.0, value=100.0)
body_temp = st.number_input("Body Temp (°C)", min_value=35.0, max_value=42.0, value=37.0)

# Convert gender to numerical
gender = 0 if gender == "Male" else 1

# Model selection
selected_model = st.selectbox("Choose a Model", list(models.keys()))

if st.button("Predict Calories"):
    model = load_model(models[selected_model])
    input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Calories Burned: {prediction:.2f}")
