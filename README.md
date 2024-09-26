# IndiOCR
## Overview
This web application allows you to upload an image, extract text from it using the EasyOCR library, and search for specific keywords within the extracted text. The app supports both English and Hindi languages for text extraction.
## Table of contents
1.[Overview](#overview)
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
```
## Setup and Deployment Guide

### Setup Instructions

#### 1. Clone the Repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-repository/ocr-text-search.git
cd ocr-text-search
```
#### 2. Install Dependencies
Ensure you have the required libraries installed:
```bash
pip install -r requirements.txt
```
#### 3. Running the App Locally
```bash
streamlit run app.py
```
#### 4. Upload an Image
- Upload an image in JPG, JPEG, or PNG format.
- Click "Extract Text" to perform OCR on the image.

#### 5. Search for Keywords
- Enter keywords in the search box and click "Search" to find matches.
- Searched Text will be highlighted.

#### 6. Download Extracted Text
- Click the button to download the extracted text as a JSON file.

## Deployment
- You can deploy this application using cloud services such as Heroku or Streamlit Cloud.

### Deployment on Streamlit Cloud:
- Create an account at [Streamlit Cloud](https://streamlit.io/cloud).
- Fork or upload your project to GitHub.
- In your Streamlit Cloud dashboard, click New app and connect your GitHub repository.

## Public Live URL
- The live URL of the deployed web application is [IndiOCR](https://indiocr.streamlit.app)
