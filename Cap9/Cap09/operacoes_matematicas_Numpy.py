import numpy as np

arr = np.arange(1,10)
print(f'\nArray: {arr}.')

# soma
print(f'\nSoma array: {np.sum(arr)}.')

# Produto
print(f'\nProduto array: {np.prod(arr)}.')

# Soma acumulada
print(f'\nSoma acumulada: {np.cumsum(arr)}.')

arr1 = np.array([3,2,1])
arr2 = np.array([1,2,3])

# Soma dos arrays
arr3 = np.add(arr1,arr2)
print(f'\nSoma dos arrays: {arr3}.')


# Criando duas matrizes
mat1 = np.array([[1,2], [3,4]])
mat2 = np.array([[5,6], [0,7]])

print(f'\nMat1 shape: {mat1.shape}.')
print(f'\nMat2 shape: {mat2.shape}.')

print(f'Mat1: {mat1}.')
print(f'Mat2: {mat2}.')

# Multiplicando as duas matrizes
mat_dot = np.dot(mat1,mat2)
print(f'Matrizes multiplicadas: \n{mat_dot}')

# Multiplicando com @ que é a mesma coisa que dot
mat_arroba = mat1 @ mat2
print(f'Matrizes multiplicadas com @: \n{mat_arroba}')

# Tensordot também multiplica
mat_tensor = np.tensordot(mat1,mat2,axes=((1),(0)))
print(f'Matrizes multiplicadas com tensordot: \n{mat_tensor}')
