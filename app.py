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

# 2. Advanced CSS Injector (Changes background to deep tech gradient and styles cards)
# 2. Advanced CSS Injector (Injects a secure background image with an interface mask)
st.markdown("""
    <style>
    /* Full-screen responsive background image with a dark tint overlay */
    .stApp {
        background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(2, 6, 23, 0.92)), 
                    url('https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1920&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #f8fafc;
    }
    
    /* Translucent frosted glass effect for Streamlit Alert/Info boxes */
    div.stAlert {
        background-color: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 12px;
        color: #e2e8f0;
    }
    
    /* Structured formatting for forensic registers */
    .stTable {
        background-color: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(6px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 8px;
    }
    
    /* Title typography gradient styling */
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }
    
    /* Section headers */
    .section-header {
        color: #38bdf8;
        font-weight: 600;
        border-left: 4px solid #818cf8;
        padding-left: 10px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)
