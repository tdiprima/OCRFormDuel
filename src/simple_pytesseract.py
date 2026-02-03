#!/usr/bin/env python3
"""
pytesseract output (Classic OCR)
"""

import numpy as np
import pytesseract
from PIL import Image

img = np.array(Image.open("w2_sample.png"))
text = pytesseract.image_to_string(img)
print("=== Simple pytesseract output ===")
print(text)
