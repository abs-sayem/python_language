# A program for converting PDF file into Doc file

# pip install pdf2docx

from pdf2docx import Converter
pdf_file = input("Pdf file name (with path if it is in other directory):")
print("Converting....")
doc_file_name = "converted2docx.docx"
converter = Converter(pdf_file)
converter.convert(doc_file_name)
converter.close()