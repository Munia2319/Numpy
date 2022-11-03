import numpy as np

arr = np.array([1, 2, 3])
print('Iterate on the elements of the following 1-D array:')

for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print('Iterate on each scalar element of the 2-D array:')

for x in arr:
  for y in x:
    print(y)
