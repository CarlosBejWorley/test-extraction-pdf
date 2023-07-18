import PyPDF2

file_path = 'pdf/text.pdf'

with open(file_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)
    
    total_pages = pdf_reader.numPages

    for page_num in range(total_pages):
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()
        print("Contenido de la página", page_num + 1)
        print(page_text)
        print("---------------------------")
    
    """ page_1 = pdf_reader.getPage(0)
    page_1_text = page_1.extractText()
    
    print(page_1_text) """