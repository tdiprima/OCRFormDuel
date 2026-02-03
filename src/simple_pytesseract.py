#!/usr/bin/env python3
"""
Simple baseline OCR using pytesseract on a W-2 form image.
Outputs flat text blob, ignoring layout/tables. For comparison with layout-aware tools.
Assumes 'w2_sample.png' image file is in the same directory.
"""

import numpy as np
import pytesseract
from PIL import Image

img = np.array(Image.open("w2_sample.png"))
text = pytesseract.image_to_string(img)
print("=== Simple pytesseract output ===")
print(text)
