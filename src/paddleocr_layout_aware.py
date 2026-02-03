#!/usr/bin/env python3
"""
Smarter Approach: PaddleOCR (Layout-Aware)
Unlike Tesseract, PaddleOCR detects each text region first (like boxes or fields) and
then applies OCR — making it layout-aware. It's built for messy, real-world docs.
"""

import matplotlib.pyplot as plt
from paddleocr import PaddleOCR
from PIL import Image, ImageDraw

img_path = "w2_sample.png"

# Initialize PaddleOCR
ocr = PaddleOCR(use_textline_orientation=True, lang="en")

# Run layout-aware OCR
result = ocr.predict(img_path)

# Extract text only
print("=== PaddleOCR Results ===")
res = result[0]
for txt in res["rec_texts"]:
    print(txt)

# Visualize detections
image = Image.open(img_path).convert("RGB")
boxes  = res["rec_polys"]
txts   = res["rec_texts"]
scores = res["rec_scores"]

# Draws the bounding polygons in red and 
# labels each one with the recognized text and confidence score.
draw = ImageDraw.Draw(image)
for box, txt, score in zip(boxes, txts, scores):
    pts = [tuple(p) for p in box]
    draw.polygon(pts, outline="red", width=2)
    draw.text(pts[0], f"{txt} ({score:.2f})", fill="red")

plt.figure(figsize=(12, 12))
plt.imshow(image)
plt.axis("off")
plt.show()
