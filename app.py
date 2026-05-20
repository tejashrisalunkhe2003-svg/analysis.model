import streamlit as st
import pickle
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NLP Prediction App",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
}

.title {
    text-align: center;
    font-size: 52px;
    font-weight: bold;
    color: #00FFD1;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from {text-shadow: 0 0 10px #00FFD1;}
    to {text-shadow: 0 0 25px #00FFD1;}
}

.box {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}

div.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(90deg,#00FFD1,#00BFFF);
    color: black;
    border: none;
}

textarea {
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    try:
        model_path = os.path.join(os.path.dirname(__file__), "nlp_model.pkl")
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

model = load_model()

# ---------------- HEADER ----------------
st.markdown('<p class="title">🤖 NLP Prediction App</p>', unsafe_allow_html=True)
st.markdown("### Enter text and get prediction instantly")

# ---------------- UI ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.subheader("📝 Enter Text")
    user_text = st.text_area(
        "Type your text here:",
        height=200,
        placeholder="Example: This product is amazing!"
    )

    predict_btn = st.button("🔮 Predict")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.subheader("📊 Prediction Result")

    if predict_btn:
        if model is not None:
            try:
                # NLP models usually expect list input
                prediction = model.predict([user_text])

                st.success(f"✅ Prediction: {prediction[0]}")
                st.balloons()

            except Exception as e:
                st.error(f"❌ Prediction Error: {e}")
        else:
            st.warning("⚠️ Model not loaded")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<center style='color:white;'>✨ Built with ❤️ using Streamlit</center>",
    unsafe_allow_html=True
)
