## Tesseract vs. PaddleOCR

### Tesseract (classic OCR)
- **How it thinks:** "Here's one big image—let me guess all the text in it."
- **Works best on:** clean, bold, simple lines of text (like a sentence on a plain page).
- **What goes wrong on W‑2s/forms:**  
  - Forms have **boxes, columns, tiny labels, rows, and alignment** → Tesseract tends to **flatten everything** into a messy blob.  
  - You get real words in some places, **gibberish in others** ("instructions" → "insimuctions").
- **Preprocessing risk (OpenCV thresholding):**
  - Thresholding can **erase faint/low-ink text** and break thin characters.
  - Result: sometimes OCR gets **worse**, even if bold text improves.

### PaddleOCR (layout-aware OCR)
- **How it thinks:** "First, find *where* text is (boxes/regions). Then read each piece."
- **Why it's better for W‑2s/invoices/receipts:**
  - Detects **text blocks/fields** instead of treating the page as one paragraph.
  - Handles **tables, multi-column layouts, and scattered labels + values** much better.
  - Often returns **bounding boxes + confidence scores**, so you can keep the structure.

## 🔍 Visual Comparison

| OCR Engine    | Layout Handling          | Common Issues                                      | Output Type                        |
| ------------- | ------------------------ | -------------------------------------------------- | ---------------------------------- |
| **Tesseract** | ❌ None                   | Merges boxes, loses structure, misreads faint text | Flat text                          |
| **PaddleOCR** | ✅ Detects boxes + layout | Slightly slower, bigger model                      | Structured blocks with coordinates |


## 🧠 TL;DR (Why This Matters)
- **Tesseract:** reads text like it's a novel.  
- **PaddleOCR:** reads text like it's a form.

## 🔗 Other resources

- `w2_sample.png` is publicly available data.

<br>
