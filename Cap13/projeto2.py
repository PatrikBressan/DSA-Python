### Versão do Python
from platform import python_version
print('\nVersão do Python:',python_version())

### Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import datetime as dt

### Carregando os dados
df_dsa = pd.read_csv('dados/dataset.csv')

# Shape
print(df_dsa.shape)

# Amostra dos dados
print(df_dsa.head())

# Amostra dos dados
print(df_dsa.tail())


### Análise Exploratória
# Colunas do conjunto de dados
print(df_dsa.columns)

# Verificando o tipo de dados de cada coluna
print(df_dsa.dtypes)

# Resumo estatístico da coluna com o valor de venda
print(df_dsa['Valor_Venda'].describe())

# Verificando se há registros duplicados
print(df_dsa.duplicated())

# Verificando se há valores ausentes
print(df_dsa.isnull().sum())

print(df_dsa.head())

###################################################################################################
### Pergunta de Negócio 1:
### Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
print('\n------------------------')
# Filtramos o dataframe com os registros da categoria que desejamos
df1 = df_dsa[df_dsa['Categoria'] == 'Office Supplies']
print(df1)

# Agrupamos por cidade e calculamos o total de valor_venda
df1_total = df1.groupby('Cidade')['Valor_Venda'].sum()
print(df1_total)

# Encontramos a cidade com maior valor de venda
cidade_maior_venda = df1_total.idxmax()
print(f'\nCidade com maior valor de venda para a categoria Office Supplies é: {cidade_maior_venda}')

# Conferindo o resultado
print(df1_total.sort_values(ascending=False))


###################################################################################################
### Pergunta de Negócio 2:
### Qual o Total de Vendas Por Data do Pedido?
### Demonstre o resultado através de um gráfico de barras.

print('\n------------------------')
df2 = df_dsa.groupby('Data_Pedido')['Valor_Venda'].sum()
print(df2.head())

# Gráfico 1
df2.plot.bar()
plt.show()

# Gráfico 2 - notação Pandas
plt.figure(figsize=(20,6))
df2.plot(x='Data_Pedido', y='Valor_Venda', color='green')
plt.title('Total de Vendas por Data do Pedido')
plt.show()


###################################################################################################
### Pergunta de Negócio 3:
### Qual o Total de Vendas por Estado?
### Demonstre o resultado através de um gráfico de barras.
print('\n------------------------')

# reset_index() ajuda na reinicialização do índice na criação de um novo data frame.
df3 = df_dsa.groupby('Estado')['Valor_Venda'].sum().reset_index()
print(df3.head())

# Gráfico 1 - notação Pandas
plt.figure(figsize=(16,6))
df3.plot(x='Estado', y='Valor_Venda', color='blue')
plt.title('Total de Vendas por Estado')
plt.show()

# Gráfico 2 - notação Seaborn
plt.figure(figsize=(14,5))
sea.barplot(data=df3,
            y='Valor_Venda',
            x='Estado').set(title='Total de Vendas por Estado')
plt.xticks(rotation = 80)
plt.show()


###################################################################################################
### Pergunta de Negócio 4:
### Quais São as 10 Cidades com Maior Total de Vendas?
### Demonstre o resultado através de um gráfico de barras.

# Solução 1
print('\n------------------------')
df4 = df_dsa.groupby('Cidade')['Valor_Venda'].sum()
dez_cidades_maior_venda = df4.nlargest(n=10)
print(f'\nAs dez cidades com maiores valores de venda são: {dez_cidades_maior_venda}')

print('\n',df4.sort_values(ascending=False))

# Solução 2
df4_2 = df_dsa.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda',
                                                                                ascending=False).head(10)

print('\nDF4_2: ', df4_2)

# Gráfico - notação Seaborn
plt.figure(figsize=(14,5))
sea.set_palette('coolwarm')
sea.barplot(data = df4_2,
            y = 'Valor_Venda',
            x = 'Cidade').set(title='10 Cidades com Maiores Valores de Venda')
plt.xticks(rotation = 80)
plt.show()