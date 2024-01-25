### Python com SQL com SQLITE
import sqlite3
print(sqlite3.sqlite_version)

import pandas as pd
print(pd.__version__)

### Conectando no BD com Linguagem Python
# conecta no BD
con = sqlite3.connect('cap12_dsa.db')

# abre um cursor para percorrer os dados no BD
cursor = con.cursor()

# Query SQL para extrair os nomes das colunas no BD
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

# Executa a query
cursor.execute(sql_query)
print(cursor.execute(sql_query))

# Vincula o resultado
cursor.fetchall()
print(cursor.fetchall())