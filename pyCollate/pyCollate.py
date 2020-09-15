# -*- coding: utf-8 -*-
"""
A python program to collate randomized exams from pdfs of different questions. 
0a) install python3 and pip3
0b) install PyPDF2 library with pip: "pip3 install pypdf2"
1) names the files 1.pdf 2a.pdf 2b.pdf 3.pdf 4a.pdf 4b.pdf etc, all in one directory
2) place this script in the same directory as the pdf files
3) run this program. Example: "python3 pyCollate.py test.pdf abca"
"""

from PyPDF2 import PdfFileMerger, PdfFileReader
import os, sys


def collate(output_pdf, nPages, key):
	origKey = key
	mergedPDF = PdfFileMerger()
	print("Writing key = " + key + "\n Collating pages:"
	for i in range(nPages):
		if(os.path.exists(str(i)+".pdf"):
			mergedPDF.append(PdfFileReader(str(i)+".pdf", 'rb'))
			print(str(i))
		elif(os.path.exists(str(i)+key[0]+".pdf"):
			mergedPDF.append(PdfFileReader(str(i)+key[0]+".pdf", 'rb'))
			print(str(i)+key[0])
			key=key[1:]
		else:
			print("Error! Both " + str(i) + ".pdf and " + str(i)+key[0] + ".pdf are not files in this directory. Examine your file names and the key : " + origKey) 
	mergedPDF.write(output_pdf)

if __name__ == "__main__":
    try: 
        output_pdf=sys.argv[1]
		nPages=int(sys.argv[2])
		key=sys.argv[3]
	except:
		print("Error! Three arguments must be supplied in commandline. Example:\n python3 pyCollate.py test.pdf 5 abc")
	collate(output_pdf, nPages, key)