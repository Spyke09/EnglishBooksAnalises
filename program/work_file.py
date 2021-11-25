import PyPDF2

pdffileobj = open('the-castrator_RuLit_Me_675747.pdf', 'rb')

pdfreader = PyPDF2.PdfFileReader(pdffileobj)
file1 = open(r"1.txt", "w")
failures = 0
for i in range(pdfreader.numPages):
    pageobj = pdfreader.getPage(i - 1)
    try:
        file1.writelines(pageobj.extractText())
    except:
        failures += 1

print(failures)
file1.close()