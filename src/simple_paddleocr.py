#!/usr/bin/env python3
"""
PaddleOCR Output (Layout-Aware OCR)
export PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK=True
"""

from paddleocr import PaddleOCR

ocr = PaddleOCR(use_textline_orientation=True, lang="en")
result = ocr.predict("w2_sample.png")

print("=== Simple PaddleOCR output ===")
for text in result[0]["rec_texts"]:
    print(text)
