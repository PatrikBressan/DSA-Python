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

### Filtrando DataFrame do Pandas com Base em Strings
print('\n-----------------------')
print(if_df.head())

# Filtramos o dataframe pela coluna Segmento com valores que iniciam com as letras 'Con'
print(if_df[if_df.Segmento.str.startswith('Con')].head())

print(if_df[if_df.Segmento.str.endswith('mer')].head())


### Split de Strings em Dataframes do Pandas
print('\n-----------------------')
print(if_df['ID_Pedido'].head())

# Temos o país, o ano e o ID do pedido. Vamos dividir essa coluna e extrair o ano para gravar em uma nova coluna
print(if_df['ID_Pedido'].str.split('-'))

print(if_df['ID_Pedido'].str.split('-').str[1].head())

# Egenharia de Atributos é chamado esse processo que fizemos
# Fazemos o split da coluna e extraímos o item na posição 2 (índice 1)
if_df['Ano'] = if_df['ID_Pedido'].str.split('-').str[1]
print(if_df.head())


### Strip de strings em dataframes do Pandas
# Split divide a string
# Strip remove caracteres da string
print('\n-----------------------')
print(if_df.head(3))

print(if_df['Data_Pedido'].head(3))

# Vamos remover os dígitos 2 (dois) e 0 (zero) à esquerda do valor da variável 'Data_Pedido'.
print(if_df['Data_Pedido'].str.lstrip('20'))

# Como não colocamos o 'inplace = True' a mudança é somente na memória e não altera o dataframe. Podemos
# usar ainda as funções rstrip() e strip() com diferentes variações de strip de strings.


### Replace de Strings em DataFrames do Pandas
# Substituímos os caracteres CG por AX na coluna 'ID_Cliente'
print('\n-----------------------')
print(if_df.head())

if_df['ID_Cliente'] = if_df['ID_Cliente'].str.replace('CG', 'AX')
print(if_df.head())


### Combinação de strings em DataFrames do Pandas
print('\n-----------------------')
print(if_df.head())

# Concatenando strings
if_df['Pedido_Segmento'] = if_df['ID_Pedido'].str.cat(if_df['Segmento'], sep = '-')
print(if_df.head())
