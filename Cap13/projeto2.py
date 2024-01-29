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