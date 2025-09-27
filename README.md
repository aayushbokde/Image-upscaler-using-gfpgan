https://huggingface.co/barisaydin/sadtalker/blob/8bcdc5e90f73d4460ad39481cb51c854eecff420/gfpgan/weights/GFPGANv1.4.pth

download link for gfpgan weights. 
# GFPGAN Image Enhancer

Enhance your images instantly using **GFPGAN** with a simple web interface powered by **Streamlit**.

---

## How to Use

1. Make sure you have Python 3.9 installed.
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the app:
    ```bash
    streamlit run app.py
    ```
4. Open the link in your browser (usually `http://localhost:8501`).
5. Upload your image and click **Enhance Image**.
6. View and download your enhanced image.

---

## Supported Image Formats

- `.jpg`
- `.jpeg`
- `.png`

---

## Notes

- The app enhances the full image, no face detection needed.
- Output images are saved in the `enhanced_img/` folder.
- Make sure the GFPGAN model weights are in the correct path:
gfpgan/weights/GFPGANv1.4.pth

---
## Quick Folder Overview

Image Upscaler/
├── app.py
├── main.py
├── gfpgan/
│ └── weights/
├── images/ # Temp uploads
├── enhanced_img/ # Enhanced images
├── requirements.txt
└── README.md




---

Enjoy your enhanced images! 🎨


# This project was made for a Company's Assignment