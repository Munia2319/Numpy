import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr = np.array(42)
arr2 = np.array([[1, 2, 3], [4,5,6]])
arr3 = np.array([[[1, 2], [3,4]], [[5,6],[7,8]]])

print('dimension: ',arr.ndim)
print('dimension: ',arr1.ndim)
print('dimension: ',arr2.ndim)
print('dimension: ',arr3.ndim)
