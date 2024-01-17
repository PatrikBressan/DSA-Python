# Utilizando Numpy e Pandas para manipulação de dados
import pandas as pd
import numpy as np

# Importa a função DataFrame do Pandas
from pandas import DataFrame


# Criando um dicionário
dados = {'Estado': ['Mato Grosso do Sul', 'Paraná', 'Santa Catarina', 'Rio Grande do Sul', 'Minas Gerais', 'São Paulo'],
         'Ano': [2019, 2020, 2021, 2022, 2023, 2024],
         'Taxa Desemprego': [1.3, 1.5, 1.7, 1.6, 2.4, 2.7]}

# Converte o dicionário em um dataframe
df = DataFrame(dados)

# Visualiza as 5 primeiras linhas
print('\n-----------------------')
print(df.head())

df2 = DataFrame(dados,
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                index = ['Estado_1', 'Estado_2', 'Estado_3', 'Estado_4', 'Estado_5', 'Estado_6'])

print('\n-----------------------')
print(df2)

print('\n-----------------------')
# Resumo estatístico do DataFrame. O resumo estatístico é a partir de dados numéricos (object não entra).
print(df2.describe())
print(df2.dtypes)

# Verificando valores ausentes
print('\n-----------------------')
print(df2.isna())
print(df2['Taxa Crescimento'].isna())

# Usando o Numpy para alimentar uma das colunas do dataframe
df2['Taxa Crescimento'] = np.arange(6.)
print('\n-----------------------')
print(df2)
print(df2.dtypes)
print(df2['Taxa Crescimento'].isna())
print(df2.describe())


# Slicing de DataFrames do Pandas
print('\n-----------------------')
print(df2['Estado_2':'Estado_4'])

print('\n-----------------------')
print(df2['Taxa Desemprego'] < 2)

print('\n-----------------------')
print(df2[ df2['Taxa Desemprego'] < 2])

print('\n-----------------------')
print(df2[['Estado', 'Taxa Crescimento']])




