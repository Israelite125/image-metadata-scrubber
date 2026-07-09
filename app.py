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

# 2. Corrected CSS Layering
st.markdown("""
    <style>
    /* Apply background to the absolute base container layer */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(2, 6, 23, 0.92)), 
                    url('https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1920&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* Make the content sheet transparent so background shines through */
    [data-testid="stHeader"], [data-testid="stAppViewBlockContainer"] {
        background-color: transparent !important;
        color: #f8fafc;
    }
    
    /* Frosted glass cards for info boxes */
    div.stAlert {
        background-color: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        border-radius: 12px;
    }
    
    /* Styled container for the forensic data tables */
    .stTable {
        background-color: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(6px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 8px;
    }
    
    /* Title typography styling */
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }
    
    /* Glowing card headers */
    .section-header {
        color: #38bdf8;
        font-weight: 600;
        border-left: 4px solid #818cf8;
        padding-left: 10px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Main Header Interface
st.title("🛡️ ExifShield Pro")
st.write("Enterprise-grade structural asset forensic audit and metadata sanitization engine.")
st.markdown("---")

# Sidebar configurations
st.sidebar.markdown("<h3 style='color: #818cf8;'>Security Rules</h3>", unsafe_allow_html=True)
max_size_mb = st.sidebar.slider("Asset Cap (MB)", 1, 10, 5)

# Layout Setup
uploaded_file = st.file_uploader("Upload Image Target Asset", type=["jpg", "jpeg"])

if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    file_size_mb = len(file_bytes) / (1024 * 1024)
    
    if file_size_mb > max_size_mb:
        st.error(f"🛑 Security Violation: File size exceeds boundaries ({file_size_mb:.2f}MB).")
    else:
        is_valid_jpeg = file_bytes.startswith(b'\xff\xd8\xff')
        
        if not is_valid_jpeg:
            st.error("🛑 Signature Mismatch: Malicious payload header suspected.")
        else:
            st.success("✅ File Structure Verified. Running analytics mapping...")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown("<p class='section-header'>🖼️ Visual Asset Preview</p>", unsafe_allow_html=True)
                original_img = Image.open(uploaded_file)
                st.image(original_img, use_container_width=True)
                
            with col2:
                st.markdown("<p class='section-header'>🕵️‍♂️ Forensic Register</p>", unsafe_allow_html=True)
                
                try:
                    exif_data = original_img.info.get('exif', b'')
                    if not exif_data:
                        st.info("No structural metadata packets discovered.")
                    else:
                        exif_dict = piexif.load(exif_data)
                        audit_log = {}
                        
                        if "0th" in exif_dict:
                            audit_log["Device Manufacturer"] = exif_dict["0th"].get(piexif.ImageIFD.Make, b"N/A").decode('utf-8', errors='ignore')
                            audit_log["Hardware Target"] = exif_dict["0th"].get(piexif.ImageIFD.Model, b"N/A").decode('utf-8', errors='ignore')
                            audit_log["Software Engine"] = exif_dict["0th"].get(piexif.ImageIFD.Software, b"N/A").decode('utf-8', errors='ignore')
                        
                        if "GPS" in exif_dict and len(exif_dict["GPS"]) > 0:
                            st.warning("🚨 VULNERABILITY ALERT: GPS Telemetry Found in Asset Header!")
                            audit_log["GPS Footprint"] = "⚠️ Active Geolocation Coordinates Leak"
                        else:
                            audit_log["GPS Footprint"] = "🔒 Protected (No Coordinates)"
                            
                        st.table(audit_log)
                        
                except Exception as e:
                    st.error(f"Analysis Fault: {e}")
                
                st.markdown("---")
                st.markdown("<p class='section-header'>⚔️ Remediation Execution</p>", unsafe_allow_html=True)
                
                if st.button("Execute Zero-Trust Purge", type="primary"):
                    with st.spinner("Scrubbing bitstream layers..."):
                        pixel_data = list(original_img.getdata())
                        clean_img = Image.new(original_img.mode, original_img.size)
                        clean_img.putdata(pixel_data)
                        
                        buffer = io.BytesIO()
                        clean_img.save(buffer, format="JPEG")
                        byte_im = buffer.getvalue()
                        
                        st.success("🔒 Remediation Successful! All EXIF data dropped.")
                        st.download_button(
                            label="📥 Download Secure Asset",
                            data=byte_im,
                            file_name="sanitized_asset.jpg",
                            mime="image/jpeg"
                        )
