#!/usr/bin/env python3
"""
Performs OCR on a W-2 form image using pytesseract with and without OpenCV preprocessing (grayscale + thresholding).
Compares raw and processed outputs to demonstrate improvements and limitations on structured documents.
Assumes 'w2_sample.png' image file is in the same directory.
"""

import cv2
import numpy as np
import pytesseract
from PIL import Image

# Load the W-2 form
img_path = "w2_sample.png"
img = np.array(Image.open(img_path))

# Basic pytesseract read
raw_text = pytesseract.image_to_string(img)
print("=== Raw pytesseract output ===")
print(raw_text)

# Preprocessing: grayscale + thresholding
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Run OCR again on thresholded image
processed_text = pytesseract.image_to_string(thresh)
print("\n=== After thresholding (OpenCV) ===")
print(processed_text)
