# Return array of odd rows and even columns from below numpy array
# sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45,48], [51 ,54, 57, 60]])

import numpy as np 

arr = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45,48], [51 ,54, 57, 60]])

O_R = arr[::2] # Odd Row
E_C = arr[:,1::2] # Even Colome

newarr = O_R[:,1::2]

print("Orinal Array:",arr)
print("-----------")

print("Odd Row",O_R)
print("-----------")

print("Even Colom",E_C)
print("-----------")

print(newarr)