import streamlit as st
import numpy as np
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🌧️ Rainfall Prediction AI",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("rainfall_model.pkl")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e3a8a,#0ea5e9);
    background-attachment: fixed;
}

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main Title */
.title{
    text-align:center;
    font-size:55px;
    font-weight:800;
    color:white;
    margin-bottom:5px;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#dbeafe;
    margin-bottom:30px;
}

/* Glass Card */
.glass{
    background:rgba(255,255,255,0.12);
    backdrop-filter:blur(15px);
    border-radius:20px;
    padding:25px;
    border:1px solid rgba(255,255,255,0.2);
    box-shadow:0 8px 30px rgba(0,0,0,0.35);
}

/* Labels */
label{
    color:white !important;
    font-weight:bold;
}

/* Inputs */
.stNumberInput input{
    border-radius:12px !important;
}

/* Button */
.stButton>button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    font-size:22px;
    font-weight:bold;
    color:white;
    background:linear-gradient(90deg,#06b6d4,#2563eb);
    transition:0.3s;
}

.stButton>button:hover{
    transform:scale(1.03);
    background:linear-gradient(90deg,#2563eb,#06b6d4);
}

/* Result Card */
.result{
    background:linear-gradient(135deg,#22c55e,#16a34a);
    color:white;
    border-radius:20px;
    padding:35px;
    text-align:center;
    font-size:35px;
    font-weight:bold;
    margin-top:30px;
    box-shadow:0px 8px 25px rgba(0,0,0,.3);
}

/* Footer */
.footer{
    text-align:center;
    color:white;
    opacity:0.8;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>🌧️ Rainfall Prediction AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Predict May Rainfall using Machine Learning</div>", unsafe_allow_html=True)

# ---------------- INPUT CARD ----------------
st.markdown("<div class='glass'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    altitude = st.number_input("🏔️ Altitude", value=30.0)
    sep = st.number_input("🌦️ September", value=1.2)
    octo = st.number_input("🍂 October", value=33.0)
    nov = st.number_input("🍁 November", value=65.0)
    dec = st.number_input("❄️ December", value=120.0)
    jan = st.number_input("🧊 January", value=150.0)

with col2:
    feb = st.number_input("🌨️ February", value=110.0)
    mar = st.number_input("🌸 March", value=75.0)
    apr = st.number_input("🌼 April", value=25.0)
    x_utm = st.number_input("📍 X UTM", value=696533.0929)
    y_utm = st.number_input("📍 Y UTM", value=3660837.106)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ---------------- PREDICTION ----------------
if st.button("🌧️ Predict Rainfall"):

    features = np.array([[
        altitude,
        sep,
        octo,
        nov,
        dec,
        jan,
        feb,
        mar,
        apr,
        x_utm,
        y_utm
    ]])

    prediction = model.predict(features)[0]

    if prediction < 50:
        status = "☀️ Low Rainfall Expected"
    elif prediction < 150:
        status = "🌦️ Moderate Rainfall Expected"
    else:
        status = "⛈️ Heavy Rainfall Expected"

    st.markdown(f"""
    <div class='result'>
        🌧️ Predicted Rainfall (May)<br><br>
        <span style='font-size:55px'>{prediction:.2f} mm</span>
        <br><br>
        <span style='font-size:28px'>{status}</span>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class='footer'>
Made with ❤️ using Streamlit • Scikit-learn • Linear Regression
</div>
""", unsafe_allow_html=True)