from camelot.io import read_pdf
import pandas as pd

file_path = 'pdf/EDS.pdf'

tables = read_pdf(file_path, pages='all')

for table in tables:
    print(table.parsing_report)
    df = table.df
    print(df)


