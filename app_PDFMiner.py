from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTTextBoxHorizontal, LTChar, LTRect, LTImage

def extract_table_elements(layout):
    table_elements = []
    for element in layout:
        if isinstance(element, LTTextContainer):
            table_elements.append(element.get_text().strip())
        elif isinstance(element, LTTextBoxHorizontal):
            table_elements.append(extract_table_elements(element))
    return table_elements

def extract_tables_from_pdf(file_path):
    tables = []
    for page_layout in extract_pages(file_path):
        table = extract_table_elements(page_layout)
        tables.append(table)
    return tables

# Ruta del archivo PDF
file_path = 'pdf/text.pdf'

# Extraer tablas del archivo PDF
tables = extract_tables_from_pdf(file_path)

# Imprimir las tablas extraídas
for table in tables:
    print(table)
