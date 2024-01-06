import numpy as np

arr = np.diag(np.arange(3))
print(arr)

print(arr[1,1])
print(arr[1])
print(arr[:,2])

arr1 = np.arange(10)
print(arr1)

#Start: end: step
print(arr1[2:9:3])

# Comparação de arrays
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])

# Comparação item a item
print(a == b)

# Comparação global
print(np.array_equal(arr,arr1))

print(arr1.min())
print(arr1.max())

# Somando um valor a cada elemento do array
print(np.array([1,2,3]) + 1.5)

arr2 = np.array([1.2, 1.5, 1.6, 2.5, 3.4, 3.5, 3.6, 4.4, 4.5, 4.6])
print(arr2)

# Método around
arr3 = np.around(arr2)
print(arr3)

# Flatten (achatando) a matriz
arr4 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr4)
array_achatado = arr4.flatten()
print(array_achatado)

# Repetindo os elementos de um array
print('\n######################')
arr5 = np.array([1,2,3])
print(arr5)
print(np.repeat(arr5,3))
print(np.tile(arr5,3))

# Cópia de um array
print('\n######################')
arr6 = np.array([5,6])
arr7 = np.copy(arr6)
print(arr6)
print(arr7)

