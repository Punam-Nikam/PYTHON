## Merging of pdfs

# from PyPDF2 
# import pdfwriter
import os

# merger=pdfwriter()
merger=()
files= [file for file in os.listdir() if
         file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.writer("Merged-pdf.pdf")
merger.close()