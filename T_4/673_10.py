# Imagine you survey your friends to find the kind of movie they like best: Comedy- 4, Action -5, Romance - 6, Drama -1, SciFi - 4. 
# Plot a pie chart for the above survey and use different color for each analysis and create a wedge for action movies. Also put as
# chart title as "Survey analysis of movie"

import matplotlib.pyplot as pil 
import numpy as np

x = np.array([4,5,6,1,4])

mylabel = ["Comedy","Action","Romance","Drama","SciFi"]

mycolor = ["Green","Red","Yellow","b","Pink"]

myexplor = [0,0.5,0,0,0]

pil.title("Survey analysis of movie")

pil.pie(x,labels=mylabel,colors=mycolor,explode=myexplor,startangle=90,autopct='%1.1f%%')

pil.show()