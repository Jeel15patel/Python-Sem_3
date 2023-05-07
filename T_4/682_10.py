# A Program to create a line graph to show the profits of a company in various years.
# The data is as mentioned: x axis as years and y axis as profits (in Millions).
# X=[2012,2013,2014,2015,2016,2017] and y = [9,10,10.5,8.8,10.9,9.75]. Plot a line
# chart with x axis as "Years" and y axis as "Profits (in Millions)" and title of the line
# chart as "XYZ Company". Also the linestyle should be dashed one.

import matplotlib.pyplot as pit 

x = [2012, 2013, 2014, 2015, 2016, 2017]
y = [9, 10, 10.5, 8.8, 10.9, 9.75]

pit.xlabel("Years")
pit.ylabel("Profits (in Millions)")
pit.title("XYZ Company")

pit.plot(x,y,linestyle="--")

pit.show()


