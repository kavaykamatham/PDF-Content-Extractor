
# AI/Python Intern Assignment – PDF Content Extraction

This project is part of the AI/Python Internship Assignment and is designed to extract **text** and **images** from a given educational PDF, and organize the content in a structured format (JSON).

## ✅ Objective

Build a Python-based tool to process an educational PDF file (e.g., Olympiad paper), extract all meaningful content, and save it in a structured way.

---

## 🗂️ Folder Structure

```
AIPython_Intern_Assignment/
├── extract_content.py                # Main script for extraction
├── app.py                            # Optional Streamlit UI for preview
├── README.md                         # This file
├── pdfs/
│   └── IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf
├── output/
    ├── extracted_content.json        # Structured output (text + image paths)
    └── images/                       # Extracted images per page
        ├── page1_image1.png
        ├── page2_image1.png
        └── ...
```

---

## 🧰 Requirements

Install dependencies using pip:

```bash
pip install PyMuPDF streamlit Pillow
```

---

## ▶️ Step-by-Step Usage

### Step 1: Add PDF File

Place the PDF file inside the `pdfs/` folder. Rename it to match:
```
pdfs/IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf
```

---

### Step 2: Run the Extraction Script

This will extract **text** and **images** from each page and save them.

```bash
python extract_content.py
```

✅ Output will be saved to:

- `output/images/` → contains extracted images like `page1_image1.png`
- `output/extracted_content.json` → contains per-page structured data

---

### Step 3 (Optional): Launch Streamlit UI

To visualize the extracted content in a friendly UI:

```bash
streamlit run app.py
```

Then open the link shown in your terminal to interact with the app.

---

## 📄 Output JSON Format

Example of a page entry in `extracted_content.json`:

```json
{
  "page": 1,
  "text": "Question 1: What comes next in the pattern?",
  "images": [
    "output/images/page1_image1.png",
    "output/images/page1_image2.png"
  ]
}
```

---

## 🙋‍♀️ Notes

- This script works best with text-based and clean PDFs.
- For scanned PDFs with no embedded text, OCR (e.g., Tesseract) would be required (not included here).
- The script automatically handles multi-page PDFs and multiple images per page.

---

## 👩‍💻 Author

Kavya Kamatham  
AI/Python Internship Assignment – 2024-25

---
