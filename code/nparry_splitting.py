import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
print('1st split',newarr[0])
print('2nd split',newarr[1])
print('3rd split',newarr[2])
