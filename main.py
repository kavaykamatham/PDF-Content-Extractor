import fitz  # PyMuPDF
import os
import json
from PIL import Image

# Paths
PDF_PATH = "pdfs/IMO_Grade_1.pdf"
IMAGE_OUTPUT_DIR = "output/images"
JSON_OUTPUT_PATH = "output/extracted_content.json"

# Ensure image output directory exists
os.makedirs(IMAGE_OUTPUT_DIR, exist_ok=True)

# Load PDF
doc = fitz.open(PDF_PATH)
extracted_data = []

for page_number in range(len(doc)):
    page = doc[page_number]
    page_text = page.get_text()
    
    # Extract images
    image_list = page.get_images(full=True)
    image_paths = []

    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_filename = f"page{page_number+1}_image{img_index+1}.{image_ext}"
        image_path = os.path.join(IMAGE_OUTPUT_DIR, image_filename)

        # Save image
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        image_paths.append(image_path)

    # Append extracted content
    extracted_data.append({
        "page": page_number + 1,
        "text": page_text.strip(),
        "images": image_paths
    })

# Save JSON
with open(JSON_OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(extracted_data, f, indent=4)

print("✅ Extraction complete. Check output folder.")
