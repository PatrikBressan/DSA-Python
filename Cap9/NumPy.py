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


# Indexação em arrays Numpy
print(arr1[4])
print(arr1[1:4])
print(arr1[1:4+1])


# Criando uma lista de índices
indices = [1, 2, 5, 6]
print(arr1[indices])

# Cria uma máscara booleana para os elementos pares
mask = (arr1 % 2 == 0)
print(f'\nMask: {mask}')
print(arr1[mask])

# Alterando um elemento do array
arr1[0] = 100
print(arr1)

# Não é possível incluir elemento de outro tipo
try:
    arr1[0] = 'Novo Elemento'
except:
    print('Operação Não Permitida!')

arr2 = np.array([1,2,3,4,5])
print(arr2)
print(arr2.cumsum())
print(arr2.cumprod())
arr3 = np.arange(0,50,5)
print(arr3)
print(type(arr3))

print(np.shape(arr3))
print(arr3.dtype)