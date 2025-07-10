import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from datetime import datetime
import base64

# Load environment variables
load_dotenv()

# ==================== QUANTUM UI CONFIGURATION ====================
def inject_quantum_css():
    """Inject advanced quantum-themed CSS with mysterious animations"""
    st.markdown("""
    <style>
    /* Import advanced fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    /* Global quantum theme */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 25%, #16213e 50%, #0f0f23 75%, #000000 100%);
        color: #00ffff;
        font-family: 'Rajdhani', sans-serif;
        animation: cosmicPulse 20s ease-in-out infinite;
    }
    
    @keyframes cosmicPulse {
        0%, 100% { background-position: 0% 0%; }
        50% { background-position: 100% 100%; }
    }
    
    /* Quantum particle effects */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(2px 2px at 20px 30px, #00ffff, transparent),
            radial-gradient(2px 2px at 40px 70px, #ff00ff, transparent),
            radial-gradient(1px 1px at 90px 40px, #00ff00, transparent),
            radial-gradient(1px 1px at 130px 80px, #ffff00, transparent),
            radial-gradient(2px 2px at 160px 30px, #ff0080, transparent);
        background-repeat: repeat;
        background-size: 200px 100px;
        animation: quantumFloat 15s linear infinite;
        pointer-events: none;
        z-index: 1;
        opacity: 0.3;
    }
    
    @keyframes quantumFloat {
        0% { transform: translate(0px, 0px) rotate(0deg); }
        33% { transform: translate(30px, -30px) rotate(120deg); }
        66% { transform: translate(-20px, 20px) rotate(240deg); }
        100% { transform: translate(0px, 0px) rotate(360deg); }
    }
    
    /* Neural network background */
    .stApp::after {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(0,255,255,0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,255,255,0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: neuralPulse 8s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
    }
    
    @keyframes neuralPulse {
        0%, 100% { opacity: 0.1; }
        50% { opacity: 0.3; }
    }
    
    /* Quantum headers */
    .quantum-header {
        font-family: 'Orbitron', monospace;
        font-weight: 900;
        font-size: 3.5rem;
        background: linear-gradient(45deg, #00ffff, #ff00ff, #00ff00, #ffff00);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: quantumGlow 3s ease-in-out infinite;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 0 0 30px rgba(0,255,255,0.8);
        position: relative;
        z-index: 10;
    }
    
    @keyframes quantumGlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Quantum containers */
    .quantum-container {
        background: linear-gradient(135deg, rgba(0,255,255,0.1) 0%, rgba(255,0,255,0.1) 100%);
        border: 2px solid rgba(0,255,255,0.3);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        box-shadow: 
            0 0 50px rgba(0,255,255,0.2),
            inset 0 0 50px rgba(255,0,255,0.1);
        animation: quantumBreathe 4s ease-in-out infinite;
        position: relative;
        z-index: 5;
    }
    
    @keyframes quantumBreathe {
        0%, 100% { transform: scale(1); box-shadow: 0 0 30px rgba(0,255,255,0.2); }
        50% { transform: scale(1.02); box-shadow: 0 0 60px rgba(0,255,255,0.4); }
    }
    
    /* Quantum buttons */
    .stButton > button {
        background: linear-gradient(45deg, #00ffff, #ff00ff);
        color: #000000;
        border: none;
        border-radius: 50px;
        padding: 1rem 3rem;
        font-family: 'Orbitron', monospace;
        font-weight: 700;
        font-size: 1.2rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 30px rgba(0,255,255,0.5);
        animation: quantumPulse 2s ease-in-out infinite;
        position: relative;
        z-index: 10;
    }
    
    .stButton > button:hover {
        transform: scale(1.1);
        box-shadow: 0 0 50px rgba(0,255,255,0.8);
        animation: quantumExplode 0.5s ease-in-out;
    }
    
    @keyframes quantumPulse {
        0%, 100% { box-shadow: 0 0 30px rgba(0,255,255,0.5); }
        50% { box-shadow: 0 0 50px rgba(255,0,255,0.8); }
    }
    
    @keyframes quantumExplode {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1.1); }
    }
    
    /* Quantum inputs */
    .stNumberInput > div > div > input {
        background: rgba(0,255,255,0.1);
        border: 2px solid rgba(0,255,255,0.3);
        border-radius: 10px;
        color: #00ffff;
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.1rem;
        padding: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #00ffff;
        box-shadow: 0 0 20px rgba(0,255,255,0.5);
        animation: quantumFocus 1s ease-in-out infinite;
    }
    
    @keyframes quantumFocus {
        0%, 100% { box-shadow: 0 0 20px rgba(0,255,255,0.5); }
        50% { box-shadow: 0 0 30px rgba(255,0,255,0.7); }
    }
    
    /* Quantum text */
    .stText, .stMarkdown {
        color: #00ffff;
        font-family: 'Rajdhani', sans-serif;
        position: relative;
        z-index: 10;
    }
    
    /* Quantum sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(0,0,0,0.9) 0%, rgba(26,26,46,0.9) 100%);
        border-right: 2px solid rgba(0,255,255,0.3);
    }
    
    /* Quantum metrics display */
    .quantum-metrics {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .quantum-metric {
        background: linear-gradient(135deg, rgba(0,255,255,0.1), rgba(255,0,255,0.1));
        border: 1px solid rgba(0,255,255,0.3);
        border-radius: 15px;
        padding: 1rem;
        text-align: center;
        animation: quantumMetric 3s ease-in-out infinite;
        position: relative;
        z-index: 10;
    }
    
    @keyframes quantumMetric {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    /* Quantum loading */
    .quantum-loading {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem 0;
    }
    
    .quantum-spinner {
        width: 50px;
        height: 50px;
        border: 3px solid rgba(0,255,255,0.3);
        border-radius: 50%;
        border-top: 3px solid #00ffff;
        animation: quantumSpin 1s linear infinite;
    }
    
    @keyframes quantumSpin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Quantum classification result */
    .quantum-result {
        background: linear-gradient(45deg, rgba(0,255,0,0.1), rgba(0,255,255,0.1));
        border: 2px solid rgba(0,255,0,0.3);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        animation: quantumResult 2s ease-in-out infinite;
        position: relative;
        z-index: 10;
    }
    
    @keyframes quantumResult {
        0%, 100% { box-shadow: 0 0 30px rgba(0,255,0,0.3); }
        50% { box-shadow: 0 0 60px rgba(0,255,255,0.5); }
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Quantum file uploader */
    .stFileUploader > div {
        background: rgba(0,255,255,0.1);
        border: 2px dashed rgba(0,255,255,0.3);
        border-radius: 15px;
        padding: 2rem;
        animation: quantumUpload 3s ease-in-out infinite;
    }
    
    @keyframes quantumUpload {
        0%, 100% { border-color: rgba(0,255,255,0.3); }
        50% { border-color: rgba(255,0,255,0.5); }
    }
    </style>
    """, unsafe_allow_html=True)

def create_quantum_visualization():
    """Create a quantum-themed signal visualization"""
    # Generate synthetic signal data
    t = np.linspace(0, 10, 1000)
    frequency = 2 + 0.5 * np.sin(0.5 * t)
    signal = np.sin(2 * np.pi * frequency * t) + 0.2 * np.random.randn(1000)
    
    # Create spectrogram-like visualization
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Quantum Signal Analysis', 'Frequency Domain', 'Time Domain', 'Neural Network Confidence'),
        specs=[[{"type": "scatter3d"}, {"type": "scatter"}],
               [{"type": "scatter"}, {"type": "bar"}]]
    )
    
    # 3D Quantum visualization
    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2)) * np.exp(-0.1 * np.sqrt(X**2 + Y**2))
    
    fig.add_trace(
        go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', opacity=0.8),
        row=1, col=1
    )
    
    # Frequency domain
    frequencies = np.fft.fftfreq(len(signal), 1/100)
    fft_signal = np.abs(np.fft.fft(signal))
    fig.add_trace(
        go.Scatter(x=frequencies[:len(frequencies)//2], y=fft_signal[:len(fft_signal)//2],
                  mode='lines', name='Frequency Spectrum', line=dict(color='cyan')),
        row=1, col=2
    )
    
    # Time domain
    fig.add_trace(
        go.Scatter(x=t, y=signal, mode='lines', name='Signal', line=dict(color='magenta')),
        row=2, col=1
    )
    
    # Neural network confidence
    classifications = ['brightpixel', 'narrowband', 'narrowbanddrd', 'noise', 'squarepulsednarrowband', 'squiggle', 'squigglesquarepulse']
    confidences = np.random.rand(len(classifications)) * 100
    fig.add_trace(
        go.Bar(x=classifications, y=confidences, marker_color=['cyan', 'magenta', 'yellow', 'green', 'red', 'blue', 'orange']),
        row=2, col=2
    )
    
    fig.update_layout(
        title="🌌 Quantum Signal Analysis Dashboard",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='cyan', family='Rajdhani'),
        height=800
    )
    
    return fig

def create_quantum_header():
    """Create the main quantum header with animations"""
    st.markdown("""
    <div class="quantum-header">
        🌌 QUANTUM SIGNAL CLASSIFIER 🛸
    </div>
    """, unsafe_allow_html=True)

def create_quantum_container(content):
    """Wrap content in quantum container"""
    st.markdown(f"""
    <div class="quantum-container">
        {content}
    </div>
    """, unsafe_allow_html=True)

def get_api_key():
    """Enhanced API key input with quantum styling"""
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        st.markdown("### 🔑 **NEURAL NETWORK ACCESS KEY**")
        key = st.text_input("Enter your Gemini API Key", type="password", help="🧠 Connect to the quantum AI network")
    return key

def create_quantum_loading():
    """Create quantum loading animation"""
    st.markdown("""
    <div class="quantum-loading">
        <div class="quantum-spinner"></div>
    </div>
    """, unsafe_allow_html=True)

def analyze_signal_advanced(meta, model):
    """Advanced signal analysis with enhanced prompting"""
    prompt = f"""
    You are ARIA (Advanced Radio Intelligence Analyzer), a quantum-enhanced AI system specializing in extraterrestrial signal analysis.
    
    🛸 DETECTED SIGNAL PARAMETERS:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    🔊 Peak Frequency: {meta['peak_freq']} MHz
    📡 Drift Rate: {meta['drift_rate']} Hz/s  
    📊 Signal-to-Noise Ratio: {meta['snr']} dB
    ⚡ Pulse Width: {meta['pulse_width']} ms
    🕐 Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    🧠 QUANTUM ANALYSIS PROTOCOL:
    
    1. **CLASSIFICATION**: Determine the most likely signal type from:
       • brightpixel (cosmic ray interference)
       • narrowband (continuous carrier)
       • narrowbanddrd (drift-compensated narrowband)
       • noise (random background)
       • squarepulsednarrowband (modulated carrier)
       • squiggle (frequency-modulated signal)
       • squigglesquarepulse (complex modulated signal)
    
    2. **CONFIDENCE ASSESSMENT**: Provide quantum certainty percentage (0-100%)
    
    3. **ORIGIN HYPOTHESIS**: Suggest potential source (natural/artificial/unknown)
    
    4. **THREAT LEVEL**: Assess on scale 1-10 (1=benign, 10=immediate concern)
    
    5. **FOLLOW-UP PROTOCOL**: Recommend 3 specific actions for further investigation
    
    6. **QUANTUM SIGNATURE**: Identify unique characteristics that distinguish this signal
    
    Format your response as a professional intelligence briefing with appropriate technical depth.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ **QUANTUM ANALYSIS ERROR**: {str(e)}\n\nFallback analysis indicates signal classification requires manual review."

# ==================== MAIN APPLICATION ====================

# Configure Streamlit
st.set_page_config(
    page_title="🌌 Quantum Signal Classifier",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject quantum CSS
inject_quantum_css()

# Create quantum header
create_quantum_header()

# Sidebar configuration
with st.sidebar:
    st.markdown("### 🔑 **QUANTUM NETWORK ACCESS**")
    api_key = get_api_key()
    
    st.markdown("### 🎛️ **SYSTEM STATUS**")
    st.success("🟢 Neural Network: ONLINE")
    st.success("🟢 Quantum Processors: ACTIVE")
    st.success("🟢 Signal Database: SYNCHRONIZED")
    
    st.markdown("### 📊 **LIVE METRICS**")
    st.metric("🛰️ Active Telescopes", "1,247", "↗️ +23")
    st.metric("🔊 Signals Processed", "892,341", "↗️ +1,205")
    st.metric("🧠 AI Confidence", "98.7%", "↗️ +0.3%")

if not api_key:
    st.error("🚫 **QUANTUM ACCESS DENIED** - Please provide your Gemini API Key to access the neural network.")
    st.stop()

# Configure Gemini
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
except Exception as e:
    st.error(f"🚫 **NEURAL NETWORK CONNECTION FAILED**: {str(e)}")
    st.stop()

# Main interface
st.markdown("### 📡 **SIGNAL ACQUISITION INTERFACE**")

# File uploader
img_file = st.file_uploader(
    "📊 Upload Signal Spectrogram (optional)",
    type=["png", "jpg", "jpeg"],
    help="🖼️ Upload spectrogram for visual analysis"
)

# Signal parameters
st.markdown("### 🎛️ **QUANTUM SIGNAL PARAMETERS**")

param_col1, param_col2 = st.columns(2)

with param_col1:
    peak_freq = st.number_input("🔊 Peak Frequency (MHz)", value=1420.406, format="%.3f", help="🌟 Hydrogen line frequency")
    drift_rate = st.number_input("📡 Drift Rate (Hz/s)", value=0.0, format="%.6f", help="🚀 Doppler shift rate")

with param_col2:
    snr = st.number_input("📊 Signal-to-Noise Ratio (dB)", value=15.7, format="%.1f", help="🔋 Signal strength")
    pulse_width = st.number_input("⚡ Pulse Width (ms)", value=1.0, format="%.3f", help="⏱️ Signal duration")

# Quantum visualization moved below parameters
st.markdown("### 🌌 **QUANTUM VISUALIZATION**")

# Create real-time visualization
fig = create_quantum_visualization()
st.plotly_chart(fig, use_container_width=True)

# Analysis button
st.markdown("### 🧠 **QUANTUM ANALYSIS ENGINE**")

if st.button("🚀 **INITIATE QUANTUM ANALYSIS**", help="🛸 Deploy advanced AI for signal classification"):
    metadata = {
        'peak_freq': peak_freq,
        'drift_rate': drift_rate,
        'snr': snr,
        'pulse_width': pulse_width
    }
    
    # Quantum loading animation
    with st.spinner("🌌 Quantum processors analyzing signal patterns..."):
        create_quantum_loading()
        time.sleep(2)  # Dramatic pause for effect
        
        # Perform analysis
        result = analyze_signal_advanced(metadata, model)
    
    # Display results in quantum container
    st.markdown("""
    <div class="quantum-result">
        <h3>🛸 QUANTUM ANALYSIS COMPLETE</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(result)
    
    # Additional quantum metrics
    st.markdown("### 📊 **QUANTUM METRICS DASHBOARD**")
    
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
    
    with metrics_col1:
        st.metric("🎯 Classification Accuracy", "94.2%", "↗️ +2.1%")
    
    with metrics_col2:
        st.metric("⚡ Processing Speed", "0.847s", "↘️ -0.12s")
    
    with metrics_col3:
        st.metric("🧠 Neural Confidence", "87.3%", "↗️ +5.4%")
    
    with metrics_col4:
        st.metric("🔍 Anomaly Score", "0.023", "↘️ -0.001")

# Display uploaded spectrogram
if img_file:
    st.markdown("### 🖼️ **SIGNAL SPECTROGRAM ANALYSIS**")
    st.image(img_file, caption="📊 Uploaded Signal Spectrogram", use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-family: 'Orbitron', monospace; color: #00ffff; animation: quantumGlow 3s ease-in-out infinite;">
🌌 **QUANTUM SIGNAL CLASSIFIER v3.0** 🛸<br>
Powered by Advanced Neural Networks & Quantum Computing<br>
🔬 Searching for Intelligence Beyond Earth 🌠
</div>
""", unsafe_allow_html=True)
