import streamlit as st
from PIL import Image
import numpy as np
import easyocr
import json
import re

class OCRModel:
    def __init__(self):
        self.reader = easyocr.Reader(['en', 'hi'])  # Initialize for English and Hindi

    def process_image(self, image: Image.Image) -> str:
        # Convert PIL Image to numpy array
        image_np = np.array(image)
        
        # Perform OCR
        result = self.reader.readtext(image_np)
        
        # Extract text from result
        text = ' '.join([item[1] for item in result])
        return text

def highlight_keywords(text, keywords):
    """Highlight the keywords in the extracted text."""
    highlighted_text = text
    for keyword in keywords:
        # Match single characters as well as whole words
        pattern = r'(?<!\w)' + re.escape(keyword) + r'(?!\w)' if len(keyword) > 1 else re.escape(keyword)
        highlighted_text = re.sub(
            pattern,
            f'<span style="background-color: yellow;">{keyword}</span>',
            highlighted_text,
            flags=re.IGNORECASE
        )
    return highlighted_text

def count_matches(text, keywords):
    """Count occurrences of each keyword in the text."""
    match_counts = {}
    for keyword in keywords:
        # Match single characters as well as whole words
        pattern = r'(?<!\w)' + re.escape(keyword) + r'(?!\w)' if len(keyword) > 1 else re.escape(keyword)
        match_counts[keyword] = len(re.findall(pattern, text, flags=re.IGNORECASE))
    return match_counts

# Initialize session state
if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = ""
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None
if 'search_keyword' not in st.session_state:
    st.session_state.search_keyword = ""
if 'search_performed' not in st.session_state:
    st.session_state.search_performed = False

st.title("Bilingual OCR Insight: Text Extraction and Search")

# Create an instance of the OCR model
@st.cache_resource
def load_ocr_model():
    return OCRModel()

ocr_model = load_ocr_model()

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.session_state.uploaded_image = Image.open(uploaded_file).convert("RGB")  # Store uploaded image
    st.image(st.session_state.uploaded_image, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract Text"):
        with st.spinner("Extracting text... This may take a moment."):
            st.session_state.extracted_text = ocr_model.process_image(st.session_state.uploaded_image)
        st.session_state.search_keyword = ""  # Reset search keyword when new text is extracted
        st.session_state.search_performed = False  # Reset search performed flag

    if st.session_state.extracted_text:
        st.subheader("Extracted Text:")
        st.write(st.session_state.extracted_text)

        # Downloadable JSON feature
        json_data = json.dumps({"extracted_text": st.session_state.extracted_text}, ensure_ascii=False, indent=4)
        st.download_button(
            label="Download Extracted Text as JSON",
            data=json_data,
            file_name="extracted_text.json",
            mime="application/json"
        )

# Only show search options if text has been extracted
if st.session_state.extracted_text:
    st.subheader("Search in Extracted Text")
    
    # Show search input for keywords
    search_keyword = st.text_input("Enter keywords to search (comma-separated):", key="search_input")
    
    # Add a search button
    if st.button("Search"):
        st.session_state.search_keyword = search_keyword
        st.session_state.search_performed = True

    # Only perform search if the search button has been clicked
    if st.session_state.search_performed and st.session_state.search_keyword:
        keywords = [k.strip() for k in st.session_state.search_keyword.split(",") if k.strip()]
        
        highlighted_text = highlight_keywords(st.session_state.extracted_text, keywords)
        st.markdown("**Highlighted Text:**", unsafe_allow_html=True)
        st.markdown(highlighted_text, unsafe_allow_html=True)

        match_counts = count_matches(st.session_state.extracted_text, keywords)
        total_matches = sum(match_counts.values())

        if total_matches > 0:
            st.write(f"Found a total of {total_matches} matches.")
            for keyword, count in match_counts.items():
                if count > 0:
                    st.markdown(f"- '{keyword}': {count} occurrences")
        else:
            st.info("No matching results found.")
