# Write a python program to create a bar plot of course v/s no. of students using the following dictionary with 
# appropriate labels for X and Y axes and colour of the bars green.
# Data={‘C’:20,’C++’:15,’Java’:30,’Python’:35}

import matplotlib.pyplot as pil 

Data={"C":20,"C++":15,"Java":30,"Python":35}

x = list(Data.keys())
y = list(Data.values())

pil.bar(x,y,color="Green")

pil.xlabel("Course")

pil.ylabel("No. of students")

pil.title("No of student per Course")

pil.show()