
import streamlit as st
import pandas as pd
import pickle

# Load model
with open("airfoil_rf_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="✈️ Airfoil Sound Prediction", page_icon="🛩️", layout="centered")

st.markdown(
    """
    <style>
    .stApp {background: linear-gradient(to right, #a1c4fd, #c2e9fb);}
    .stButton>button {background-color:#0d47a1;color:white;font-weight:bold;border-radius:10px;padding:10px 20px;}
    .prediction-card {background: #ffefba; padding: 20px; border-radius: 15px; text-align:center; font-size:1.5em; font-weight:bold;}
    </style>
    """, unsafe_allow_html=True
)

st.title("✈️ Airfoil Sound Prediction App")
st.markdown("Predict the **scaled sound pressure level** (dB) of an airfoil using input parameters.")

# Sidebar inputs
st.sidebar.header("🛠 Input Parameters")
frequency = st.sidebar.slider("Frequency (Hz)", 70, 20000, 1000)
aoa = st.sidebar.slider("Angle of Attack (deg)", -5.0, 15.0, 5.0)
chord = st.sidebar.slider("Chord Length (m)", 0.05, 0.25, 0.1)
velocity = st.sidebar.slider("Velocity (m/s)", 30.0, 100.0, 50.0)
thickness = st.sidebar.slider("Displacement Thickness (m)", 0.0005, 0.02, 0.005)

input_data = pd.DataFrame({
    'Frequency': [frequency],
    'Angle_of_attack': [aoa],
    'Chord_length': [chord],
    'Velocity': [velocity],
    'Displacement_thickness': [thickness]
})

# Prediction
prediction = model.predict(input_data)[0]

st.markdown(f"""
<div class="prediction-card">
🔊 Predicted Sound Pressure Level: <span style='color:#0d47a1'>{prediction:.2f} dB</span>
</div>
""", unsafe_allow_html=True)
