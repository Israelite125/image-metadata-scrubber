import streamlit as st
from PIL import Image

# 1. Page Configuration & UI Layout
st.set_page_config(page_title="PrivacyClean", page_icon="🛡️", layout="centered")

st.title("🛡️ Privacy Clean: Image Metadata Scrubber")
st.write("Social media platforms and messaging apps don't always strip your camera and location details. Upload any JPEG photo below to strip its hidden metadata before you share it.")

st.info("🔒 **100% Private:** Your files are processed dynamically in memory and are never stored permanently on a server.")

# 2. File Uploader Widget
uploaded_file = st.file_uploader("Drag and drop or browse a JPEG image...", type=["jpg", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image file
    original_img = Image.open(uploaded_file)
    
    # Display a preview of the image to the user
    st.image(original_img, caption="Uploaded Image Preview", use_container_width=True)
    
    # 3. The Scrubbing Action Button
    if st.button("Scrub My Image", type="primary"):
        with st.spinner("Sanitizing image pixels..."):
            # Replicate the pixel data to drop the metadata wrapper completely
            pixel_data = list(original_img.getdata())
            clean_img = Image.new(original_img.mode, original_img.size)
            clean_img.putdata(pixel_data)
            
            # Save the clean image into a temporary bytes buffer so the user can download it
            import io
            buffer = io.BytesIO()
            clean_img.save(buffer, format="JPEG")
            byte_im = buffer.getvalue()
            
            st.success("🔒 Your image has been successfully sanitized! Click below to save it.")
            
            # 4. Provide a Download Button
            st.download_button(
                label="📥 Download Clean Image",
                data=byte_im,
                file_name="clean_anonymous_photo.jpg",
                mime="image/jpeg"
            )
