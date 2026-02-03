#!/usr/bin/env python3
"""
Classic Approach: pytesseract + OpenCV
This version treats the entire image as one big blob of text.
No understanding of layout, columns, or text zones.
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
