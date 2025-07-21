import streamlit as st
import json
import os
from PIL import Image

st.set_page_config(page_title="PDF-Based Question Generator", layout="wide")
st.title("📘 PDF-Based Question Generator")

# Load extracted JSON
with open("output/extracted_content.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

tab1, tab2 = st.tabs(["📄 View Extracted Text", "🖼️ View Extracted Images"])

with tab1:
    st.header("📄 Page-wise Extracted Text")
    for page in pages:
        with st.expander(f"Page {page['page']}"):
            st.text_area("Text", page['text'], height=200)

with tab2:
    st.header("🖼️ Extracted Images by Page")
    for page in pages:
        st.subheader(f"📄 Page {page['page']}")
        if page["images"]:
            cols = st.columns(len(page["images"]))
            for i, img_path in enumerate(page["images"]):
                with cols[i]:
                    if os.path.exists(img_path):
                        st.image(Image.open(img_path), width=250)
                    else:
                        st.warning(f"Image not found: {img_path}")
        else:
            st.info("No images found on this page.")
