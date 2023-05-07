# Sort following NumPy array
# Case 1: Sort array by the second row
# Case 2: Sort the array by the second column
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

import numpy as np 

arr = np.array([[34,43,73],[82,22,12],[53,94,66]])

case_1 = np.argsort(arr[1])
case1_arr = arr[:,case_1]
print("Case 1:",case1_arr)

case_2 = np.argsort(arr[:,1])
case2_arr = arr[case_2]
print("Case 2:",case2_arr)