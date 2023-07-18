from tabula.io import read_pdf
from tabulate import tabulate
import pandas as pd

file_path = 'pdf/xd.pdf'

# Lee las tablas en el archivo PDF
tables = read_pdf(file_path, pages='6', multiple_tables=True)

# Itera sobre las tablas extraídas
for i, table in enumerate(tables):
    # Convierte la tabla en un DataFrame de Pandas
    df = pd.DataFrame(table)
    
    # Imprime el DataFrame de Pandas
    print(f"Tabla {i+1}:")
    print(df)
    print("----")