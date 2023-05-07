# Following is the provided numPy array. Return array of items by taking the third column from all rows
# sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

import numpy as np 

arr = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
print("Orinal Array:",arr)

print("Taking the Third Column from all Rows")
newarr = arr[:,2]
print(newarr)
