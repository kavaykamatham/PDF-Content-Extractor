import fitz  # PyMuPDF
import os
import json

# Input/output paths
pdf_path = "pdfs/IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"
output_dir = "output"
image_dir = os.path.join(output_dir, "images")
os.makedirs(image_dir, exist_ok=True)

# Load PDF
doc = fitz.open(pdf_path)
extracted = []

# Loop through each page
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()
    page_images = []

    for img_index, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]

        # Save image
        image_filename = f"page{page_num + 1}_image{img_index + 1}.{image_ext}"
        image_path = os.path.join(image_dir, image_filename)
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        page_images.append(image_path.replace("\\", "/"))  # ensure cross-platform

    extracted.append({
        "page": page_num + 1,
        "text": text.strip(),
        "images": page_images
    })

# Save structured JSON
json_path = os.path.join(output_dir, "extracted_content.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(extracted, f, indent=2, ensure_ascii=False)

print("✅ Text and images extracted successfully.")
