import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
def get_api_key():
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        key = st.text_input("Enter your Gemini API Key", type="password")
    return key

# Initialize Streamlit app
st.set_page_config(page_title="🚀 Signal Classifier with Gemini", layout="centered")
st.title("🔭 Radio Signal Classifier & Insights")

# Sidebar: API key
with st.sidebar:
    st.header("🔑 API Configuration")
    api_key = get_api_key()

if not api_key:
    st.warning("Please provide your Gemini API Key to continue.")
    st.stop()

# Configure Gemini client
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# Main inputs
st.header("📥 Upload & Metadata Input")
img_file = st.file_uploader("Upload Signal Spectrogram (optional)", type=["png", "jpg", "jpeg"])

# Collect metadata fields
st.subheader("📊 Signal Metrics")
col1, col2 = st.columns(2)
with col1:
    peak_freq = st.number_input("Peak Frequency (MHz)", value=1420.0, format="%.2f")
    drift_rate = st.number_input("Drift Rate (Hz/s)", value=0.0, format="%.2f")
with col2:
    snr = st.number_input("Signal-to-Noise Ratio", value=10.0, format="%.2f")
    pulse_width = st.number_input("Pulse Width (ms)", value=1.0, format="%.2f")

# Classify button
def analyze_signal(meta):
    prompt = f"""
You are a radio-astronomy expert.
Here are the observed signal metrics:
- Peak frequency: {meta['peak_freq']} MHz
- Drift rate: {meta['drift_rate']} Hz/s
- Signal-to-noise ratio: {meta['snr']}
- Pulse width: {meta['pulse_width']} ms

Tasks:
1. Classify this signal into one of: brightpixel, narrowband, narrowbanddrd, noise, squarepulsednarrowband, squiggle, squigglesquarepulse.
2. Provide a confidence percentage.
3. Suggest three follow-up observations or analyses.
"""
    response = model.generate_content(prompt)
    return response.text

if st.button("🚀 Classify & Get Insights"):
    metadata = {
        'peak_freq': peak_freq,
        'drift_rate': drift_rate,
        'snr': snr,
        'pulse_width': pulse_width
    }
    with st.spinner("Analyzing signal with Gemini..."):
        result = analyze_signal(metadata)
    st.subheader("🛰️ Classification & Insights")
    st.markdown(result)

# Optionally show uploaded image
if img_file:
    st.image(img_file, caption="Uploaded Spectrogram", use_column_width=True)
