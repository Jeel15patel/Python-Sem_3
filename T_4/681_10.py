# Uncle Bruno owns a garden with 30 black cherry trees. Each tree is of a different height. 
# The height of the trees (in inches): 
# 61, 63, 64, 66, 68, 69, 71, 71.5, 72, 72.5, 
# 73, 73.5, 74, 74.5, 76, 76.2, 76.5, 77, 77.5, 
# 78, 78.5, 79, 79.2, 80, 81, 82, 83, 84, 85, 87.
# Plot a histogram with color green, title of the chart should be height of trees along with it’s fontsize as 20.

import matplotlib.pyplot as pit 

heights = [ 61, 63, 64, 66, 68, 69, 71, 71.5, 72, 72.5, 73, 73.5, 74, 74.5, 76, 
            76.2, 76.5, 77, 77.5, 78, 78.5, 79, 79.2, 80, 81, 82, 83, 84, 85, 87]

pit.hist(heights,bins=5,color="Green")

pit.xlabel("Height (inches)",)
pit.ylabel("Frequency")
pit.title("Height of Trees",fontsize=20)

pit.show()