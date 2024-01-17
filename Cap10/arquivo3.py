### Preenchendo valores ausentes em DataFrames no Pandas
#A função fillna() é usada para preencher os valores ausentes
import pandas as pd
import numpy as np

from pandas import DataFrame

# Importando um dataset
if_df = pd.read_csv("dataset.csv")

print('\n-----------------------')
print(if_df.head(5))

print('\n-----------------------')
print(if_df.isna().sum())

# Extraímos a moda da coluna Quantidade. Moda em estatística é uma medida de tendência central,
# que representa o valor mais frequente em um conjunto de dados.
moda = if_df['Quantidade'].value_counts().index[0]

print('\n-----------------------')
print(moda)

if_df['Quantidade'].fillna(value = moda, inplace = True)
print('\n-----------------------')
print(if_df.isna().sum())



### Query (consulta) de dados no DataFrame do Pandas
'''
Com o Pandas criamos dataframes, que são essencialmente tabelas. Como tal, podemos
fazer consultas, ou simplesmente queries. E para isso usamos o método query().
'''
print('\nQuery 1 -----------------------')
print(if_df.Valor_Venda.describe())

# Vamos fazer uma consulta que retorne todas as vendas dentro de um range de valores.
# Geramos um novo dataframe apenas com o intervalo de vendas entre 229 e 10.000
print('\nQuery 2 -----------------------')
df2 = if_df.query('229 < Valor_Venda < 10000')
print(df2.Valor_Venda.describe())

# Geramos um novo dataframe apenas com o intervalo de vendas acima da média
print('\nQuery 3 -----------------------')
df3 = df2.query('Valor_Venda > 766')
print(df3.head())

# Shape retorna nº de linhas e nº de colunas
print('\n-----------------------')
print(if_df.shape)

print(if_df['Quantidade'].isin([5,7,9,11]))

print('\n Shape com Filtro')
print(if_df[if_df['Quantidade'].isin([5,7,9,11])].shape)
print(if_df[if_df['Quantidade'].isin([5,7,9,11])][:10])


# Operadores lógicos para Manipulação de Dados com Pandas
print('\n-----------------------')
# head = cabeça = retorna os primeiros valores
print(if_df[ (if_df.Segmento == 'Home Office') & (if_df.Regiao == 'South') ].head())
# tail = cauda = retorna os últimos valores
print(if_df[ (if_df.Segmento == 'Home Office') | (if_df.Regiao == 'South') ].tail())

print(if_df[ (if_df.Segmento != 'Home Office') & (if_df.Regiao != 'South') ].sample(5))

# Agrupamento de Dados em DataFrames com GroupBy
print('\n-----------------------')
print(if_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean())

# Agregação Múltipla com GroupBy
print('\n-----------------------')
print(if_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count']))
