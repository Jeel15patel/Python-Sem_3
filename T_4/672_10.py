# Here is how many students got each grade in the recent test:A- 4, B-12, C-10, D-2. Plot a pie chart for the student grades 
# in the recent chart with different colors for each student grades and create a wedge for D. Also put a chart title
# as student's grade history.


import matplotlib.pyplot as pil 
import numpy as np

x = np.array([4,12,10,2])
mylabel = ["A","B","C","D"]
mycolor = ["Red","Yellow","b","Pink"]
myexplor = [0,0,0,0.5]
pil.title("student's grade history")
pil.pie(x,labels=mylabel,colors=mycolor,explode=myexplor,startangle=90,autopct='%1.1f%%')
pil.show()