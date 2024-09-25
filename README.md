# EasyOCR and Text Search App

This web application allows you to upload an image, extract text from it using the EasyOCR library, and search for specific keywords within the extracted text. The app supports both English and Hindi languages for text extraction.

## Features
- **Image Upload**: Upload an image (JPG, JPEG, PNG formats) for text extraction.
- **Text Extraction**: Extract text from the uploaded image using EasyOCR.
- **Keyword Search**: Search for specific keywords in the extracted text.
- **Highlighting**: Highlight matching keywords in the extracted text.
- **Match Count**: Display the number of occurrences of each keyword.
- **Downloadable JSON**: Download the extracted text as a JSON file.

## Requirements

### Python Version:
- Python 3.8 or above

### Libraries:
- **Install the required Python libraries with the following command**:
```bash
pip install streamlit easyocr Pillow numpy
-**Streamlit**: For building the web app interface.
-**EasyOCR**: For Optical Character Recognition (OCR).
-**Pillow**: For image handling.
-**Numpy**: For image conversion.
-**re (Regex)**: Used for keyword searching and highlighting.

## Setup
-**Clone the Repository**: Clone this repository to your local machine.
