#!/usr/bin/env python3
"""
Layout-aware OCR on a W-2 form using PaddleOCR: detects text regions, extracts text, and visualizes bounding boxes.
Superior for structured docs like forms with tables/boxes. Includes optional visualization.
Assumes 'w2_sample.png' image file is in the same directory.
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
