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

# Criando gráficos com seaborn
# Carregando um dos datasets que vem com o Seaborn
dados = sea.load_dataset('tips')
print(dados.head())

# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
sea.jointplot(data=dados, x='total_bill', y='tip', kind='reg')
plt.show()

# O método lmplot() cria plot com dados e modelos de regressão
sea.lmplot(data=dados, x='total_bill', y='tip', col='smoker')
plt.show()

# Construindo um dataframe com Pandas
df = pd.DataFrame()

# Alimentando o DataFrame com valores aleatórios
df['idade'] = random.sample(range(20, 100), 30)
df['peso'] = random.sample(range(55,150), 30)

print(df.shape)
print(df.head())

# lmplot
sea.lmplot(data=df, x='idade', y='peso', fit_reg=True)
plt.show()

# kdeplot
sea.kdeplot(df.idade)
plt.show()

sea.kdeplot(df.peso)
plt.show()

# displot
sea.distplot(df.peso)
plt.show()

# Histograma
plt.hist(df.idade, alpha=.3)
sea.rugplot(df.idade)
plt.show()

# Box Plot
sea.boxplot(df.idade, color='m')
plt.show()

sea.boxplot(df.peso, color='y')
plt.show()

# Violin Plot
sea.violinplot(df.idade, color='g')
plt.show()

sea.violinplot(df.peso, color='cyan')
plt.show()

# Clustermap
sea.clustermap(df)
plt.show()