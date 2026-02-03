#!/usr/bin/env python3
"""
Simple layout-aware OCR using PaddleOCR on a W-2 form.
Detects and prints text blocks separately, preserving structure better than classic OCR.
Assumes 'w2_sample.png' image file is in the same directory.
"""

from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="en")
result = ocr.ocr("w2_sample.png", cls=True)

print("=== Simple PaddleOCR output ===")
for line in result[0]:
    print(line[1][0])
