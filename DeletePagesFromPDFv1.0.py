#!/usr/bin/env python

#This is small auto Python script file to instead of deleting pages, create a new document and add all pages which you don't want to delete.
#If you want to delete pages, iterate over the pages in your source PDF and skip over the pages to be deleted as you write your new PDF.
#Created by Tommas Huang 
#Created date: 2019-07-24

from PyPDF2 import PdfFileWriter, PdfFileReader
#The work may involve processing pdf files. PyPDF2 is a library that can easily handle pdf files. It provides operations such as reading, writing, splitting, merging, and file conversion.

pages_to_delete = [799, 800] 
#PDF to delete page numbering starts from 0
infile = PdfFileReader('/Users/TommasHuang/Desktop/Test3/deeplearningbook.pdf', 'rb')
#Open the PDF to be delete page file path.
output = PdfFileWriter()
#This class supports writing PDF files out.

for i in range(infile.getNumPages()):
#Calculate the number of pages in this PDF file.
    if i not in pages_to_delete:
    #Check if something is (not) in a list in.
        p = infile.getPage(i)
        output.addPage(p)
        #output file is a copy of the source.
with open('newpdffile.pdf', 'wb') as f:
    output.write(f)
#Save delete pdf page to new pdf file path.