# Laurell had visited a zoo recently and had collected the following data. How can Laurell use a scatter 
# plot to represent this data? .Take Type of Animal as X-axis and no. in Y axis. 
# The data is as follows: Zebra-25, Lions- 5, Monkeys- 50, Elephants -10, Ostriches - 20

import matplotlib.pyplot as pit 
import numpy as np
 
y = np.array([25,5,50,10,20])
x = np.array(["Zebra","Lions","Monkeys","Elephants","Ostriches"])

pit.scatter(x,y)

pit.ylabel("No of Animal")
pit.xlabel("Name of Animal")

pit.show()