**# Text-Parsing**


The code is a Python script that performs Optical Character Recognition (OCR) on a PDF document using the PyMuPDF and pytesseract libraries. Here's a brief explanation of what the code does:

**Install Dependencies:** The code begins by updating the system and installing the necessary libraries and dependencies for the OCR process.

**Download and Install Poppler:** Poppler is a PDF rendering library. The code downloads the Poppler source code, extracts it, and builds and installs it on the system.

**Install pytesseract:** pytesseract is a Python wrapper for the Tesseract OCR engine. The code installs the pytesseract library using pip.

**Install Tesseract:** Tesseract is the OCR engine used by pytesseract. The code installs the Tesseract OCR engine on the system.

**Import Libraries:** The necessary libraries, including pytesseract and fitz (PyMuPDF), are imported.

**Load PDF and Perform OCR:** The code loads a PDF file using fitz (PyMuPDF) and sets a zoom factor for increased resolution. It then iterates over each page of the PDF, converts it to an image, and performs OCR using pytesseract. The extracted text is printed and saved to a text file.


**# Readme:**

**Description:** Provide a brief overview of the project and mention that the code performs OCR on a PDF using PyMuPDF and pytesseract.

**Dependencies:** List the dependencies required to run the code, including pytesseract, PyMuPDF, and Tesseract.

**Installation:** Explain the installation steps, such as updating the system, installing the necessary libraries, and downloading Poppler and Tesseract.

**Usage:** Describe how to use the code, including any specific input requirements or file paths. Mention that the OCR output is printed and saved to a text file.
