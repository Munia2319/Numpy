import numpy as np

arr = np.array([1, 2, 3, 4])
arr1 = np.array([[1,2,3,4], [5,6,7,8]])
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3= np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(arr[0])
print('2nd element on 1st row of 2D array:', arr1[0, 1])
print('Element on 1st row of 3D array:', arr2[0, 1, 2])
print('Last element from 2nd dim:', arr3[1, -1])
