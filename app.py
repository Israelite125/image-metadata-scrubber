import streamlit as st
from PIL import Image
import piexif
import io

# 1. Page Configuration
st.set_page_config(
    page_title="ExifShield Pro", 
    page_icon="🛡️", 
    layout="wide"
)

# 2. Hardened Live Video Background HTML & CSS
st.markdown("""
    <style>
    /* Absolute base selectors to force transparency over the video layer */
    html, body, [data-testid="stAppViewContainer"], .main, [data-testid="stHeader"] {
        background-color: transparent !important;
        background: transparent !important;
        color: #f8fafc;
    }
    
    /* Fixed background container for the video element */
    #video-background {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: -9999; /* Sends it to the absolute bottom layer */
        object-fit: cover;
        opacity: 0.18; /* Subtle cyber animation opacity */
        pointer-events: none;
    }
    
    /* Content wrapper tuning to prevent overlapping layout limits */
    [data-testid="stAppViewBlockContainer"] {
        background-color: transparent !important;
    }
    
    /* Frosted glass styling for metrics and info containers */
    div.stAlert, div[data-testid="stMetricValue"] {
        background-color: rgba(15, 23, 42, 0.65) !important;
        backdrop-filter: blur(12px);
        border-radius: 12px;
    }
    
    div.stAlert {
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
    }
    
    .stTable {
        background-color: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 8px;
    }
    
    /* Title text styling */
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }
    
    .section-header {
        color: #38bdf8;
        font-weight: 600;
        border-left: 4px solid #818cf8;
        padding-left: 10px;
        margin-bottom: 15px;
    }
    </style>
    
    <video autoplay loop muted playsinline id="video-background">
        <source src="https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-screens-and-numbers-31948-large.mp4" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)

# 3. Application Interface Header
st.title("🛡️ ExifShield Pro")
st.write("Enterprise-grade structural asset forensic audit and metadata sanitization engine.")
st.markdown("---")

# FEATURE 1: Real-Time Security Metrics Row
m1, m2, m3 = st.columns(3)
with m1:
    st.metric(label="Global Assets Sanitized", value="14,281", delta="+312 this week")
with m2:
    st.metric(label="Threat Signatures Deflected", value="98.4%", delta="0.2% improvement")
with m3:
    st.metric(label="Avg Processing Latency", value="14ms", delta="-2ms optimization")
st.markdown("---")

# 4. Sidebar Configuration Engine
st.sidebar.markdown("<h3 style='color: #818cf8;'>Security Controls</h3>", unsafe_allow_html=True)
max_size_mb = st.sidebar.slider("Asset Cap Boundary (MB)", 1, 10, 5)

# FEATURE 2: Global Threat Feed Sidebar Simulation
st.sidebar.markdown("---")
st.sidebar.markdown("<h4 style='color: #38bdf8;'>🌐 Global Nodes Feed</h4>", unsafe_allow_html=True)
st.sidebar.caption("🤖 Node_Lagos: Sanitized asset_9921.jpg (Clean)")
st.sidebar.caption("🔥 Node_Abuja: Deflected Malicious File Signature (Dropped)")
st.sidebar.caption("🤖 Node_Akure: Stripped GPS Telemetry from asset_4402.jpg")

# 5. Core Operational File Pipeline
uploaded_file = st.file_uploader("Upload Image Target Asset for Forensic Mapping", type=["jpg", "jpeg"])
