# Versão da Linguagem Python
from platform import python_version
print(f'Versão da Linguagem Python utilizada neste código é: {python_version()}')

import numpy as np
print(f'Version Numpy: {np.__version__}')

#Criando arrays a partir de uma lista em Python
arr1 = np.array([10, 21, 32, 43, 48, 15, 76, 57, 89])
print(arr1)
print(type(arr1))

# nº de linhas, nº de colunas, nº da profundidade, ...
# Vetor = 1 dimensão
# Matriz = 2 dimensões
# Imagem 3D = 3 dimensões
print(arr1.shape)
