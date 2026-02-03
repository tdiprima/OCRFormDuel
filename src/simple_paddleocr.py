#!/usr/bin/env python3
"""
PaddleOCR Output (Layout-Aware OCR)
"""

from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="en")
result = ocr.ocr("w2_sample.png", cls=True)

print("=== Simple PaddleOCR output ===")
for line in result[0]:
    print(line[1][0])
