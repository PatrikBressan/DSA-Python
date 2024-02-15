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


###################################################################################################
### Pergunta de Negócio 5:
### Qual Segmento Teve o Maior Total de Vendas?
### Demonstre o resultado através de um gráfico de pizza.

print('\n\n------------------------')
print('\nPERGUNTA DE NEGÓCIO 5')
df5 = df_dsa.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda', ascending=False)
print(f'\nSegmento com Maior Total de Vendas é: \n{df5}')

# Função para converter os dados em valor absoluto
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format

# Plot
plt.figure(figsize=(16,6))
plt.pie(df5['Valor_Venda'],
        labels=df5['Segmento'],
        autopct=autopct_format(df5['Valor_Venda']),
        startangle=90)

# Limpa o círculo central
centre_circle = plt.Circle((0,0), 0.82, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Labels e anotações
plt.annotate(text='Total de Vendas: ' + '$ ' + str(int(sum(df5['Valor_Venda']))), xy=(-0.25, 0))
plt.title('Total de Vendas por Segmento')
plt.show()

#values = df5[[0,1],[1,1],[2,1],[3,1]]
#labels = df5[[0,0],[1,0],[2,0],[3,0]]
#print(f'\n Values: {values} - Labels: {labels}')


#print('\nShape DF5: ', df5.shape)
#plt.pie

#df.groupby('species').count().plot.pie(y='sepal length (cm)')

# Gráfico - notação Seaborn
#sea.set_style('whitegrid')
#plt.figure(figsize=(16,6))
#plt.pie(df5[1], labels=df5[0], autopct='%1.2f%%', startangle=90, shadow=True, explode=(0.2,0,0,0))
#plt.show()

#plt.pie(fatias, labels= atividades, colors=cores,autopct='%1.2f%%', startangle=90, shadow=True, explode=(0,0.2,0,0))
#df.groupby('species').count().plot.pie(y='sepal length (cm)')

###################################################################################################
### Pergunta de Negócio 6 (Desafio Nível Baby):
### Qual o Total de Vendas Por Segmento e Por Ano?
print('\n\n------------------------')
print('\nPERGUNTA DE NEGÓCIO 6')

### Split de strings
df_dsa['Ano'] = df_dsa['Data_Pedido'].str.split('/').str[2]
print(f'\nDF6: {df_dsa}')


df6 = df_dsa.groupby(['Segmento', 'Ano'])['Valor_Venda'].sum()
print(f'\nDF6: {df6}')

df6_ano_primeiro = df_dsa.groupby(['Ano','Segmento'])['Valor_Venda'].sum()
print(f'\nDF6: {df6_ano_primeiro}')


###################################################################################################
### Pergunta de Negócio 7 (Desafio Nível Júnior):
'''
Os gestores da empresa estão considerando conceder diferentes faixas de descontos
e gostariam de fazer uma simulação com base na regra abaixo:
- Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
- Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
### Quantas Vendas Receberiam 15% de Desconto?
'''
print('\n\n------------------------')
print('\nPERGUNTA DE NEGÓCIO 7')
# Opção 1
df7 = df_dsa.query('Valor_Venda > 1000').count()
print(f'\nA quantidade de vendas que podem receber 15% de desconto é: {df7}.')

# Opção 2 - resposta aprimorada
# Cria uma nova coluna de acordo com a regra da pergunta de negócio 7
df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10)
print('\n',df_dsa.head())

# Total por cada valor da variável
print('\n', df_dsa['Desconto'].value_counts())

###################################################################################################
### Pergunta de Negócio 8 (Desafio Nível Master):
'''
Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior.
Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?
'''
print('\n\n------------------------')
print('\nPERGUNTA DE NEGÓCIO 8')

# Criamos uma coluna calculando o valor de venda menos o desconto
df_dsa['Valor_Venda_Desconto'] = df_dsa['Valor_Venda'] - (df_dsa['Valor_Venda'] * df_dsa['Desconto'])
df_dsa.head()

# Filtramos as vendas antes do desconto de 15%
df8_vendas_antes_desconto = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda']

# Filtramos as vendas depois do desconto de 15%
df8_vendas_depois_desconto = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda_Desconto']

# Calculamos as médias das vendas antes e depois do desconto de 15%
media_vendas_antes_desconto = df8_vendas_antes_desconto.mean()
media_vendas_depois_desconto = df8_vendas_depois_desconto.mean()

# Imprimimos
print(f'\nMédia do valor de venda antes do desconto de 15%: {round(media_vendas_antes_desconto,2)}')
print(f'\nMédia do valor de venda depois do desconto de 15%: {round(media_vendas_depois_desconto,2)}')



###################################################################################################
### Pergunta de Negócio 9 (Desafio Nível Master Ninha):
'''
Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?

Demonstre o resultado através de gráfico de linha.
'''
print('\n\n------------------------')
print('\nPERGUNTA DE NEGÓCIO 9')

# Calculamos a a média de vendas por segmento
df9_segmento = df_dsa.groupby('Segmento')['Valor_Venda'].mean()

# Pegamos o ano na pergunta de negócio 5
# Calculamos a média de vendas por ano
df9_ano = df_dsa.groupby('Ano')['Valor_Venda'].mean()

# Precisamos criar uma coluna do dataframe com o mês
df_dsa['Mes'] = df_dsa['Data_Pedido'].str.split('/').str[1]
print(df_dsa.head)


