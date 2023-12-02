import numpy as np
print(f'Version Numpy: {np.__version__}')

arr1 = np.array([[1,2,3], [4,5,6]])
print(arr1)
print(arr1.shape)

arr2 = np.ones((2,3))
print(arr2)

lista = [[13,81,22], [0,34,59], [21,48,94]]
print(type(lista))
arr3 = np.matrix(lista)
print(type(arr3))
print(arr3)
print(np.shape(arr3))
print(arr3.size)
print(arr3.dtype)
print(arr3)
print(arr3[2,1])

print(arr3[0:2,2])
print(arr3[1,])

arr3[1,0] = 100
print(arr3)

# Deixando o Numpy decidir o tipo de dado
x = np.array([1, 2])
y = np.array([1.0, 2.0])

# Forçando o tipo de dado específico
z = np.array([1, 2], dtype = np.float64)

print(x.dtype, y.dtype, z.dtype)

arr4 = np.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype=float)
print(arr4.dtype)
print(arr4)
print('\nItem Size', arr4.itemsize)
print(arr4.nbytes)
print(arr4.ndim)