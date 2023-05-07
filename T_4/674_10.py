# Create a Pie Chart using Python Program for the popularity data of different programming languages and displayed it as a pie chart using 
# the Matplotlib Python library. For Python- 29, Java – 19, Javascript – 8, C.sharp - 7, PHP – 6, C,C++ - 5, R – 3.
# Create an exploded view of python and show the % of each programming language in Pie Chart.

import matplotlib.pyplot as pil 
import numpy as np

x = np.array([29,19,8,7,6,5,3])

mylabel = ["Python","Java","Javascript","C.sharp","PHP","C,C++","R"]

myexplor = [0.2,0,0,0,0,0,0]

pil.title("The Popularity data of different programming languages")

pil.pie(x,labels=mylabel,explode=myexplor,startangle=90,autopct='%1.1f%%')

pil.show()