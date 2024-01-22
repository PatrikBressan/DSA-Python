### Construção de gráficos a partir do DataFrames do Pandas
import sklearn
print(sklearn.__version__)

# Importando dataset Iris
from sklearn.datasets import load_iris
data = load_iris()

# Carregamos o dataset iris como dataframe do Pandas
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(data['data'], columns = data['feature_names'])
df['species'] = data['target']
print(df.head())

# Criar um gráfico de linhas com todas as variáveis do dataframe
#df.plot()
#plt.show()

# Plotar scatter plot
df.plot.scatter(x=2,y=1)
plt.show()

columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df[columns].plot.area()
plt.show()

# Calculamos a média das colunas agrupando pela coluna species e criamos um gráfico de barras com o resultado
df.groupby('species').mean().plot.bar()
plt.show()

# Ou então, fazemos a contagem de classes da coluna species e plotamos em gráfico de pizza
df.groupby('species').count().plot.pie(y='sepal length (cm)')
plt.show()

# Gráfico KDE (Kernel Density Function)
df.plot.kde(subplots=True, figsize=(8,8))
plt.show()

# Boxplot
columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df[columns].plot.box(figsize = (8,8))
plt.show()

