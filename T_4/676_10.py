# Create a bar chart for the following dataset: 
# Country =['USA','Canada','Germany','UK','France']
# GDP_Per_Capita = [45000,42000,52000,49000,47000]. 
# Also plot title, X-Axis, Y-Axis,different color for each country and the grid should be visible

import matplotlib.pyplot as pit

Country = ['USA','Canada','Germany','UK','France'] # x
GDP_Per_Capita = [45000,42000,52000,49000,47000] # y
colors = ["Red","Black","Green","Orange","Yellow"]

pit.xlabel("Country")
pit.ylabel("GDP_Per_Capita")
pit.title('GDP Per Capita by Country')
pit.grid(True)

pit.bar(Country,GDP_Per_Capita,color=colors)

pit.show()