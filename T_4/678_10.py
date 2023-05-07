# Write a program to build two bar graphs using subplot function for given two dictionaries in which one graph is in 
# 1st row and another in second row which is horizontal representation of bar graph.
# D1={“aryan”:66,”bob”:70,”jack”:66,”seema”:34}
# D2={“joy”:45,”sid”:85,”hina”:90}
# And also make a title of graph at top as “BAR PLOT

import matplotlib.pyplot as pit

D1 = {"aryan":66,"bob":70,"jack":66,"seema":34}
D2 = {"joy":45,"sid":85,"hina":90}

x_1 = list(D1.keys())
y_1 = list(D1.values())

x_2 = list(D2.keys())
y_2 = list(D2.values())

pit.suptitle("BAR PLOT")

pit.subplot(2,1,1)
pit.barh(x_1,y_1,color="Green")
pit.ylabel("Name")
pit.xlabel("Scores")
pit.title("Graph 1")

pit.subplot(2,1,2)
pit.barh(x_2,y_2,color="Red")
pit.ylabel("Name")
pit.xlabel("Scores")
pit.title("Graph 2")

pit.show()