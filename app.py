import streamlit as st
import numpy as np
import json
import pickle
import os

# Set up paths targeting your artifacts folder
MODEL_PATH = os.path.join("artifacts", "bangalore_home_prices_model.pickle")
COLUMNS_PATH = os.path.join("artifacts", "columns.json")


@st.cache_resource
def load_assets():
    with open(COLUMNS_PATH, "r") as f:
        data_columns = json.load(f)['data_columns']
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return data_columns, model


try:
    data_columns, model = load_assets()
    locations = data_columns[3:]
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

# ─── 🎨 CUSTOM COLORFUL CSS INJECTION ───
st.markdown("""
    <style>
    /* Gradient Title Animation */
    .gradient-text {
        background: linear-gradient(90deg, #ff007f, #7928ca, #00ffcc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle-text {
        color: #94a3b8;
        text-align: center;
        font-size: 16px;
        margin-bottom: 30px;
    }
    /* Colorful Neon Prediction Box Layout */
    .prediction-card {
        background: linear-gradient(135deg, rgba(121, 40, 202, 0.2), rgba(0, 255, 204, 0.1));
        border: 2px solid #00ffcc;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0px 0px 25px rgba(0, 255, 204, 0.2);
    }
    .price-value {
        color: #ff007f;
        font-size: 36px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ─── 🖼️ FRONTEND UI LAYOUT ───
st.markdown('<p class="gradient-text">🏡 Bangalore Estate Value Predictor</p>',
            unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Harnessing Machine Learning to compute instant property valuations</p>',
            unsafe_allow_html=True)

# Wrap inputs inside a colorful container/expander or clean layout cards
with st.container(border=True):
    st.subheader("📊 Property Matrix Parameters")

    selected_location = st.selectbox(
        "📍 Target Location / Neighborhood", options=[loc.title() for loc in locations])
    total_sqft = st.number_input(
        "📐 Total Square Feet Area", min_value=300, max_value=10000, value=1200, step=50)

    col1, col2 = st.columns(2)
    with col1:
        bhk = st.slider("🛏️ Total BHK (Bedrooms)",
                        min_value=1, max_value=6, value=2)
    with col2:
        bath = st.slider("🚿 Total Bathrooms", min_value=1,
                         max_value=6, value=2)

# ─── 🚀 INFERENCE EXECUTION LOGIC ───
if st.button("🔮 Calculate Estimated Market Value", type="primary", use_container_width=True):
    try:
        loc_index = data_columns.index(selected_location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    predicted_price = model.predict([x])[0]

    # Render custom styled, colorful container block for results
    st.markdown(f"""
        <div class="prediction-card">
            <h3 style="margin: 0; color: #f8fafc;">📊 Valuation Assessment Complete</h3>
            <p style="margin: 10px 0; color: #cbd5e1; font-size: 18px;">Estimated Valuation Matrix Scale:</p>
            <div class="price-value">₹ {round(predicted_price, 2)} Lakhs</div>
        </div>
    """, unsafe_allow_html=True)
