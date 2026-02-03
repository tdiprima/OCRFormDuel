#!/usr/bin/env python3
"""
Smarter Approach: PaddleOCR (Layout-Aware)
Unlike Tesseract, PaddleOCR detects each text region first (like boxes or fields) and
then applies OCR — making it layout-aware. It's built for messy, real-world docs.
"""

import matplotlib.pyplot as plt
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

img_path = "w2_sample.png"

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="en")

# Run layout-aware OCR
result = ocr.ocr(img_path, cls=True)

# Extract text only
print("=== PaddleOCR Results ===")
for line in result[0]:
    print(line[1][0])

# Visualize detections
image = Image.open(img_path).convert("RGB")
boxes = [line[0] for line in result[0]]
txts = [line[1][0] for line in result[0]]
scores = [line[1][1] for line in result[0]]

im_show = draw_ocr(image, boxes, txts, scores, font_path=None)
plt.figure(figsize=(12, 12))
plt.imshow(im_show)
plt.axis("off")
plt.show()
