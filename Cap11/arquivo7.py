### Statistical Data Visualization com Seaborn em Python
import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Seaborn roda acima do matplotlib, por isso também utilizá-lo
import seaborn as sea

# Valores randômicos
np.random.seed(42)
n = 1000
pct_smokers = 0.2 # porcentagem de pessoas fumantes

# Variáveis
flag_fumante = np.random.rand(n) < pct_smokers
#print(f'\nFlag Fumante: {flag_fumante}')
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

# DataFrame
dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})

# Cria os dados para a variável flag_fumante
dados['flag_fumante'] = dados['flag_fumante'].map({True: 'Fumante', False: 'Não Fumante'})

print(dados.shape)
print(dados.head())


# Style
sea.set(style = 'ticks')

#lmplot
sea.lmplot(x = 'altura',
           y = 'peso',
           data = dados,
           hue = 'flag_fumante',
           palette = ['tab:blue', 'tab:orange'],
           height = 7)

# Labels e título
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação Entre Altura e Peso de Fumantes e Não Fumantes.')

# Remove as bordas
sea.despine()

plt.show()
