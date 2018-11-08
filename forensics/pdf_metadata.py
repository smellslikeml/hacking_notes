#!/usr/bin/env python
from PyPDF2 import PdfFileReader


def printMeta(fileName):
    pdfFile = PdfFileReader(open(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print('[*] PDF MetaData For: ' + str(fileName))
    for metaItem in docInfo:
        print('[+] ' + metaItem + ':' + docInfo[metaItem])

if __name__ == '__main__':
    import sys
    pdf = sys.argv[1]
    printMeta(pdf)
