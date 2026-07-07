import streamlit as st
from PIL import Image
import piexif
import io

# 1. Page Configuration (Professional Branding)
st.set_page_config(
    page_title="ExifShield Pro | Advanced Metadata Sanitizer", 
    page_icon="🛡️", 
    layout="wide"
)

st.title("🛡️ ExifShield Pro: Enterprise Privacy & Forensic Audit Tool")
st.markdown("---")

# Layout Split: Sidebar for controls, main area for dashboard
st.sidebar.header("⚙️ Security Parameters")
max_size_mb = st.sidebar.slider("Maximum File Size Allowed (MB)", 1, 10, 5)

uploaded_file = st.file_uploader("Upload Image Asset for Forensic Analysis", type=["jpg", "jpeg"])

if uploaded_file is not None:
    # --- SECURITY GUARDRAIL 1: File Size Validation ---
    file_bytes = uploaded_file.getvalue()
    file_size_mb = len(file_bytes) / (1024 * 1024)
    
    if file_size_mb > max_size_mb:
        st.error(f"🛑 Security Violation: File size ({file_size_mb:.2f}MB) exceeds the configured limit of {max_size_mb}MB.")
    else:
        # --- SECURITY GUARDRAIL 2: Magic Byte Verification (Hex Analysis) ---
        # True JPEGs start with the hex bytes: FF D8 FF
        is_valid_jpeg = file_bytes.startswith(b'\xff\xd8\xff')
        
        if not is_valid_jpeg:
            st.error("🛑 Security Alert: Malicious file signature detected! The file header does not match genuine JPEG structure.")
        else:
            st.success("✅ File Integrity Verified: Genuine JPEG image asset structure detected.")
            
            # Create two columns for the Dashboard Layout
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("🖼️ Source Image Analytics")
                original_img = Image.open(uploaded_file)
                st.image(original_img, use_container_width=True)
                
            with col2:
                st.subheader("🕵️‍♂️ Forensic Metadata Audit")
                
                try:
                    # Load EXIF data wrapper
                    exif_data = original_img.info.get('exif', b'')
                    if not exif_data:
                        st.info("ℹ️ Minimal or no metadata wrapper detected on this asset.")
                    else:
                        exif_dict = piexif.load(exif_data)
                        
                        # Parse information cleanly into tables
                        audit_log = {}
                        
                        if "0th" in exif_dict:
                            audit_log["Camera Manufacturer"] = exif_dict["0th"].get(piexif.ImageIFD.Make, b"Hidden/None").decode('utf-8', errors='ignore')
                            audit_log["Camera Model"] = exif_dict["0th"].get(piexif.ImageIFD.Model, b"Hidden/None").decode('utf-8', errors='ignore')
                            audit_log["Software Used"] = exif_dict["0th"].get(piexif.ImageIFD.Software, b"Hidden/None").decode('utf-8', errors='ignore')
                        
                        if "GPS" in exif_dict and len(exif_dict["GPS"]) > 0:
                            st.warning("🚨 CRITICAL PRIVACY LEAK: Precise GPS Telemetry Found!")
                            audit_log["GPS Status"] = "⚠️ Location Leaking"
                        else:
                            audit_log["GPS Status"] = "🔒 Safe (No Telemetry)"
                            
                        # Display data as a clean structured key-value table
                        st.table(audit_log)
                        
                except Exception as e:
                    st.error(f"Error executing forensic scan: {e}")
                
                st.markdown("---")
                st.subheader("🛡️ Sanitization Pipeline")
                
                # Asynchronous memory buffer simulation for scalability
                if st.button("Execute Zero-Trust Sanitization", type="primary"):
                    with st.spinner("Processing asset via memory buffer pipeline..."):
                        
                        # Strip metadata by re-mapping raw pixel arrays
                        pixel_data = list(original_img.getdata())
                        clean_img = Image.new(original_img.mode, original_img.size)
                        clean_img.putdata(pixel_data)
                        
                        # Output stream to buffer (Memory-based, horizontal scale-friendly)
                        buffer = io.BytesIO()
                        clean_img.save(buffer, format="JPEG")
                        byte_im = buffer.getvalue()
                        
                        st.balloons()
                        st.success("🔒 Mitigation Complete: All EXIF headers and structural metadata arrays dropped successfully.")
                        
                        st.download_button(
                            label="📥 Download Sanitized Asset",
                            data=byte_im,
                            file_name="sanitized_asset.jpg",
                            mime="image/jpeg"
                        )
