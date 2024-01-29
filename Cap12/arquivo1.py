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


### A query abaixo retorna todas as linhas e todas as colunas da tabela
# Cria uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa'

# Executa a query no BD
cursor.execute(query1)

# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]

# Visualiza o resultado
print(f'\nNome das colunas: {nomes_colunas}')

# Retorna os dados da execução da query
dados = cursor.fetchall()

# Visualiza os dados
print(f'\nDados: {dados}')


### Aplicando a Linguagem SQL direto no BD com Linguagem Python
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'

# Executa a query no BD
cursor.execute(query2)

# Visualiza o resultado
print(cursor.fetchall())


### Cria uma instrução SQL para calcular a média de unidade vendidas por protudo,
### quando o valor unitário for maior que 189
query3 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
          FROM tb_vendas_dsa
          WHERE Valor_Unitario > 199
          GROUP BY Nome_Produto"""

cursor.execute(query3)

print(cursor.fetchall())

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()