## Text-Parsing


The code is a Python script that performs Optical Character Recognition (OCR) on a PDF document using the PyMuPDF and pytesseract libraries. Here's a brief explanation of what the code does:

**Install Dependencies:** The code begins by updating the system and installing the necessary libraries and dependencies for the OCR process.

**Download and Install Poppler:** Poppler is a PDF rendering library. The code downloads the Poppler source code, extracts it, and builds and installs it on the system.

**Install pytesseract:** pytesseract is a Python wrapper for the Tesseract OCR engine. The code installs the pytesseract library using pip.

**Install Tesseract:** Tesseract is the OCR engine used by pytesseract. The code installs the Tesseract OCR engine on the system.

**Import Libraries:** The necessary libraries, including pytesseract and fitz (PyMuPDF), are imported.

**Load PDF and Perform OCR:** The code loads a PDF file using fitz (PyMuPDF) and sets a zoom factor for increased resolution. It then iterates over each page of the PDF, converts it to an image, and performs OCR using pytesseract. The extracted text is printed and saved to a text file.


## Readme

**Description:**

The code performs Optical Character Recognition (OCR) on a PDF document.
It utilizes the PyMuPDF and pytesseract libraries in Python.

**Dependencies:**

pytesseract (version 0.3.9)
PyMuPDF
Tesseract OCR engine

**Installation:**

Update the system using apt update.
Install the required system libraries using apt-get install.
Download and build the Poppler library from source.
Install pytesseract using pip install pytesseract==0.3.9.
Install the Tesseract OCR engine using apt install tesseract-ocr and apt install libtesseract-dev.
Install PyMuPDF using pip install PyMuPDF.

**Usage:**

Run the code and it will perform OCR on the PDF, extracting the text.
The extracted text will be printed to the console and saved to a text file named "FileName.txt".

**License:**

pytesseract: pytesseract library is released under the Apache License 2.0. You can find the license details in the library's documentation or source code.

tesseract-ocr: tesseract-ocr is an open-source OCR engine. It is released under the Apache License 2.0 as well. You can find more information about the license in the tesseract-ocr repository or its documentation.

PyMuPDF: PyMuPDF is a Python wrapper for the MuPDF library. MuPDF itself is released under the GNU Affero General Public License (AGPL). It's important to review the specific terms and conditions of the MuPDF license to ensure compliance.

MIT License
