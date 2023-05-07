# A Bar Chart to display employee id numbers on X-axis and their salaries as Y-axis in the form of a bar graph for two departments of a company. 
# There are two departments like sales department and purchase department. 
# For sales department their id's and salaries are mentioned as : 
# x= [1001,1003,1006,1007,1009,1011] and  y=[10000, 23000.50,18000.33,16500.5,12000.75, 9999.99] 
# purchase department their id's and salaries are mentioned as: 
# x=[100̣2,1004,1010,1008,1014,1015] and y=[ 5000,6000,4500.5,12000,9000,10000].
# Make the chart title as "Microsoft Inc.", x-axis as emplyee id and Y axis as Salary. Use
# different colors for sales and purchase department.

import matplotlib.pyplot as pit 
import numpy as np 

X_S = [1001,1003,1006,1007,1009,1011]
Y_S = [10000, 23000.50,18000.33,16500.5,12000.75, 9999.99] 

X_P = [1002,1004,1010,1008,1014,1015] 
Y_P = [ 5000,6000,4500.5,12000,9000,10000]

pit.xlabel("Emplyee ID")
pit.ylabel("Salary")
pit.title("Microsoft Inc")

pit.bar(X_S,Y_S,color="Green", label="Sales Department")
pit.bar(X_P,Y_P,color="Red", label="Purchase Department")

pit.legend()

pit.show()