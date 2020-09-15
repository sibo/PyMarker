# -*- coding: utf-8 -*-
"""
A python program to collate randomized exams from pdfs of different questions. 
0a) install python3 and pip3
0b) install PyPDF2 library with pip: "pip3 install pypdf2"
1) names the files 1.pdf 2a.pdf 2b.pdf 3.pdf 4a.pdf 4b.pdf etc, all in one directory
2) place this script in the same directory as the pdf files
3) run this program. Example: "python3 pyCollate.py test.pdf [numberOfPDFfiles] ab"
"""

from PyPDF2 import PdfFileMerger, PdfFileReader
import os, sys


def collate(output_pdf, nPages, key):
	origKey = key
	mergedPDF = PdfFileMerger()
	print("input key = " + key + "\n Collating pages:")
	for j in range(nPages):
		i = j + 1
		if(os.path.exists(str(i)+".pdf")):
			mergedPDF.append(PdfFileReader(str(i)+".pdf", 'rb'))
			print(str(i),end=" ")
		elif(os.path.exists(str(i)+key[0]+".pdf")):
			mergedPDF.append(PdfFileReader(str(i)+key[0]+".pdf", 'rb'))
			print(str(i)+key[0],end=" ")
			key=key[1:]
		else:
			print("Error! Both " + str(i) + ".pdf and " + str(i)+key[0] + ".pdf are not files in this directory. Examine your file names and the key : " + origKey) 
	mergedPDF.write(output_pdf)
	print("complete!")

if __name__ == "__main__":
	try: 
		firstArg=sys.argv[1]
	except:
		print("Error! The first command line argument must be a .pdf or .csv file. Examples: \"python3 pyCollate.py exams.csv 3\" or \"python3 pyCollate.py test.pdf 3 ab\"
	if (firstArg[-4:]==".pdf"):
		output_pdf = firstArg
		try:
			nPages=int(sys.argv[2])
			key=sys.argv[3]
		except:
			print("Error! Three arguments must be supplied in commandline. Example:\n python3 pyCollate.py test.pdf 3 ab")
		collate(output_pdf, nPages, key)
    elif (firstArg[-4:]==".csv"):
		try:
			nPages=int(sys.argv[2])
		except:
			print("Error! Two arguments must be supplied in commandline. Examples: \"python3 pyCollate.py exams.csv 3\"")
		import csv
        with open(firstArg) as csv_file:
            csv_reader = csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                collate(row[0]+".pdf",nPages,row[1])
    else:
        print("Error! The first command line argument must be a .pdf or .csv file. Examples: \"python3 pyCollate.py exams.csv 3\" or \"python3 pyCollate.py test.pdf 3 ab\"
