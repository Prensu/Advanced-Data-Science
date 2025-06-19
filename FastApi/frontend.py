import streamlit as st
import requests
import base64

# ========== CONFIG ========== #
API_URL = "http://localhost:8000/predict"
st.set_page_config(page_title="Insurance Predictor", page_icon="💼", layout="centered")

# ========== HEADER ========== #
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            text-align: center;
            color: #3E64FF;
            font-weight: bold;
        }
        .subtext {
            font-size: 18px;
            text-align: center;
            color: #444;
            margin-bottom: 30px;
        }
        .stButton button {
            background-color: #3E64FF;
            color: white;
            border: none;
            padding: 0.5em 1.5em;
            font-size: 16px;
            border-radius: 8px;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #2e4bcc;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💼 Insurance Premium Category Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Please enter your information below to get a personalized prediction</div>', unsafe_allow_html=True)

# ========== FORM ========== #
with st.form(key="input_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🎂 Age", min_value=1, max_value=119, value=30)
        weight = st.number_input("⚖️ Weight (kg)", min_value=1.0, value=65.0)
        height = st.number_input("📏 Height (m)", min_value=0.5, max_value=2.5, value=1.7)
        smoker = st.selectbox("🚬 Do you smoke?", options=[True, False])

    with col2:
        income_lpa = st.number_input("💰 Annual Income (LPA)", min_value=0.1, value=10.0)
        city = st.text_input("🌆 City", value="Mumbai")
        occupation = st.selectbox(
            "💼 Occupation",
            ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
        )

    submit = st.form_submit_button("🚀 Predict Premium Category")

# ========== PREDICTION ========== #
if submit:
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    with st.spinner("Contacting prediction engine... 🔍"):
        try:
            response = requests.post(API_URL, json=input_data)
            if response.status_code == 200:
                result = response.json()
                st.success(f"🎯 Predicted Insurance Premium Category: **{result['predicted_category']}**")
            else:
                st.error(f"❌ API Error: {response.status_code} - {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("🚫 Unable to connect to FastAPI server. Make sure it's running at `localhost:8000`.")

# ========== FOOTER ========== #
st.markdown("---")
st.markdown("<center><small>Crafted with ❤️ using Streamlit</small></center>", unsafe_allow_html=True)
