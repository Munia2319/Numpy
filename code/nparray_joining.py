import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

'''concatenate--
Join a sequence of arrays along an existing axis.

stack--
Join a sequence of arrays along a new axis.'''

arr = np.concatenate((arr1, arr2))
arr3 = np.dstack((arr1, arr2))


print('joining using concatenate function: ',arr)
print('joining using dstack function: ',arr3)
