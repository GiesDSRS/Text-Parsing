# -*- coding: utf-8 -*-
"""Pytesseract_with_fitz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EUzjxeOdfc2kg7igz966Dd4oX5vne1oW
"""

!apt update
!apt-get install libnss3 libnss3-dev
!apt-get install libcairo2-dev libjpeg-dev libgif-dev
!apt-get install cmake libblkid-dev e2fslibs-dev libboost-all-dev libaudit-dev

!wget https://poppler.freedesktop.org/poppler-21.09.0.tar.xz;
!tar -xvf poppler-21.09.0.tar.xz;

!mkdir -p poppler-21.09.0/build && \
cd poppler-21.09.0 && \
cmake  -DCMAKE_BUILD_TYPE=Release   \
       -DCMAKE_INSTALL_PREFIX=/usr  \
       -DTESTDATADIR=$PWD/testfiles \
       -DENABLE_UNSTABLE_API_ABI_HEADERS=ON && \
make && \
make install

!pip install pytesseract==0.3.9

!apt install tesseract-ocr
!apt install libtesseract-dev
!pip install tesseract

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

!pip install PyMuPDF

import fitz

pdffile = "/G60754101-OTHERS(2)-2021.pdf"
doc = fitz.open(pdffile)

from PIL import Image

zoom = 3 # to increase the resolution
mat = fitz.Matrix(zoom, zoom)

for page in doc:
  pix = page.get_pixmap(matrix = mat)
  img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
  txt = pytesseract.image_to_string(img, lang='eng')
  print(txt)
  with open("/G60754101-OTHERS(2)-2021.txt", "a") as text_file:
    text_file.write(txt)