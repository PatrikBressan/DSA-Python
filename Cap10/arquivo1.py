import pandas as pd
print(pd.__version__)

# Criando um dicionário
dados = {'Estado': ['Mato Grosso do Sul', 'Paraná', 'Santa Catarina', 'Rio Grande do Sul', 'Minas Gerais', 'São Paulo'],
         'Ano': [2019, 2020, 2021, 2022, 2023, 2024],
         'Taxa Desemprego': [1.3, 1.5, 1.7, 1.6, 2.4, 2.7]}

# Importa a função DataFrame do Pandas
from pandas import DataFrame

# Converte o dicionário em um dataframe
df = DataFrame(dados)

# Visualiza as 5 primeiras linhas
print(df.head())

print(type(df))

# Reorganizando as colunas
print(DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano']))

# Criando outro dataframe com os mesmos dados anteriores mas adicionando uma coluna
df2 = DataFrame(dados,
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                index = ['Estado_1', 'Estado_2', 'Estado_3', 'Estado_4', 'Estado_5', 'Estado_6'])


print(df2)

print('\n-----------------------')
print(df2.values)

print('\n-----------------------')
print(df2.dtypes)

# Imprimindo as colunas
print('\n-----------------------')
print(df2.columns)

# Imprimindo apenas uma coluna
print('\n-----------------------')
print(df2['Estado'])

# Python é case sensitive: dá erro
# print('\n-----------------------')
# print(df2['estado'])

# Imprimindo apenas duas colunas do Dataframe.
# Obs: duas ou + colunas deve vir dentro de abre e fecha colchetes
print('\n-----------------------')
print(df2[['Taxa Desemprego', 'Ano']])

# Filtrando pelo índice
print('\n-----------------------')
print(df2.index)

# Filtrando pelo índice
print('\n-----------------------')
print(df2.filter(items=['Estado_3'], axis=0))