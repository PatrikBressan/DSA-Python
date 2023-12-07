import numpy as np
import os

filename = os.path.join('Cap9\dataset.csv')
arr = np.loadtxt(filename, delimiter=',', usecols= (0,1,2,3), skiprows = 1)
print(arr)

print(type(arr))

# Carregando apenas duas variáveis (colunas) do arquivo
var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(0,1), skiprows=1, unpack=True)
print('\n',var1)
print('\n',var2)

# Gerando um plot a partir de um arquivo usando o Numpy
import matplotlib.pyplot as plt
plt.plot(var1, var2, 'o', markersize = 6, color = 'red')
plt.show()