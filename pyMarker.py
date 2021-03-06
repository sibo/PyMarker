# -*- coding: utf-8 -*-
"""
A python program to watermark pdfs with array of names. 
0a) install python3 and pip3
0b) install fpdf, PyPDF2, and Pillow libraries with pip: "pip3 install fpdf pypdf2 pillow"
1) edit the "names" array and the dpiRes (resolution)
2) place this script in the same directory as your exam.pdf 
3) run this program: "python3 pyMarker.py examName.pdf" or "python3 pyMarker.py examName.pdf text" (optional 'text' argument keeps text highlightable)
"""

from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
from PIL import Image
import os, sys

names=["Sibo Lin","John Smith"]
dpiRes=200

def watermark(input_pdf, output_pdf, watermark_pdf):
    watermark = PdfFileReader(watermark_pdf)
    watermark_page = watermark.getPage(0)
    pdf = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()
    
    for page in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)
    
    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

def pdf2jpg2pdf(input):
    print("converting from pdf to jpg to pdf: " + input)       
    pages = convert_from_path(input,dpi=dpiRes)
    imageList=[]
    prefix=os.path.splitext(input)[0]+'_'
    for i in range(len(pages)):
        pages[i].save(prefix+str(i)+'.jpg', 'JPEG')
        img = Image.open(prefix+str(i)+'.jpg')
        img = img.convert('RGB')
        if i != 0:
            imageList.append(img)
        os.remove(prefix+str(i)+'.jpg')
    imageList[0].save(prefix+'img.pdf', save_all=True, append_images=imageList) 

if __name__ == "__main__":
    try: 
        examPDF=sys.argv[1]
        for name in names:
            name += " "
            repeated=name*20000
            
            pdf = FPDF()
            pdf.add_page()
            textsize=3
            pdf.set_font("Helvetica",style='I',size=textsize)
            pdf.set_text_color(0,0,0) 
            pdf.write(h=textsize/3,txt=repeated)
            #save watermark as PDF
            pdf.output("watermark.pdf")
            
            #merge exam and watermark PDFs
            output=examPDF[0:-4]+'_'+name.replace(" ","")+'.pdf'            
            watermark(input_pdf=examPDF, 
                          output_pdf=output,
                          watermark_pdf='watermark.pdf')
            os.remove('watermark.pdf')
                          
            """ unless "text" argument is given, convert pdfs to graphics so that text is non-selectable. 
            150dpi filesizes are ~4x larger
            200dpi filesizes are ~8x larger
            300dpi filesizes are ~20x larger. 
            """
            if(sys.argv[-1] == "text"):
              print("text in PDFs remain highlightable!")
            else:             
              pdf2jpg2pdf(output) 
              #below line removes pdf with selectable text
              os.remove(output)
    except:
      print("Error! .pdf file must be supplied in command. Examples:\n python3 pyMarker.py exam_chem.pdf \n python3 pyMarker.py exam_chem.pdf text")
