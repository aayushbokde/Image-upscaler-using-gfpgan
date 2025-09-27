import streamlit as st
import numpy as np
import cv2
import os
from main import enhance_image  # import GFPGAN enhancement

OUTPUT_DIR = "enhanced_img"
os.makedirs(OUTPUT_DIR, exist_ok=True)

st.set_page_config(page_title="GFPGAN Image Enhancer", layout="centered")
st.title("GFPGAN Image Enhancer")
st.write("Upload an image to enhance it using GFPGAN.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.subheader("Original Image")
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption='Uploaded Image', use_container_width=True)

    if st.button('Enhance Image'):
        # Save temp input image
        input_path = os.path.join('images', uploaded_file.name)
        os.makedirs('images', exist_ok=True)
        cv2.imwrite(input_path, img)

        # Output path
        output_path = os.path.join(OUTPUT_DIR, f"enhanced_{uploaded_file.name}")

        # Run GFPGAN enhancement
        enhanced_img = enhance_image(input_path, output_path, upscale=4)

        st.subheader("Enhanced Image")
        st.image(cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2RGB), caption='Enhanced Image', use_container_width=True)

        # Download button
        with open(output_path, "rb") as file:
            st.download_button(
                label="Download Enhanced Image",
                data=file,
                file_name=f"enhanced_{uploaded_file.name}",
                mime="image/jpeg"
            )
