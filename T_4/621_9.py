# Print max from axis 0 and min from axis 1 from the following 2-D array.
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

import numpy as np 

arr = np.array([[34,43,73],[82,22,12],[53,94,66]])

max0 = np.max(arr,axis=0)
print(max0)

min1 = np.min(arr,axis=1)
print(min1)