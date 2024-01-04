import numpy as np

arr = np.array([15,23,63,94,75])

# Média
media = np.mean(arr)
print(f'\nMédia: {media}.')

# Desvio padrão - Standard Deviation
std = np.std(arr)
print(f'\nDesvio padrão: {std}.')

# Variância
var = np.var(arr)
print(f'\nVariância: {var}.')
