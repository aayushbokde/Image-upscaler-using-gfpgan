import cv2
import numpy as np
import os
from gfpgan import GFPGANer

# Initialize GFPGAN globally
restorer = GFPGANer(
    model_path="C:/Users/aayus/Downloads/Image Upscaler/gfpgan/weights/GFPGANv1.4.pth",
    upscale=4,
    arch='clean',
    channel_multiplier=2,
    bg_upsampler=None
)


def enhance_image(input_image_path, output_image_path, upscale=4):
    """
    Enhance an image using GFPGAN (full-image enhancement, no face detection).
    
    Args:
        input_image_path (str): Path to input image.
        output_image_path (str): Path to save enhanced image.
        upscale (int): Upscaling factor (2 or 4).
    """
    # Load image
    img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Image not found: {input_image_path}")

    # GFPGAN enhancement (full image)
    _, _, output = restorer.enhance(
        img,
        has_aligned=False,
        only_center_face=False,
        paste_back=True
    )

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    cv2.imwrite(output_image_path, output)
    print(f"✅ Enhanced image saved at {output_image_path}")

    return output
