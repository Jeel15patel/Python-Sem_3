# A program to display a histogram showing the number of employees in specific age groups. The data is shown:
# emp_ages=[22,45,30,59,58,56,57,45,43,43,50,40,34,33,25,19] and their 
# bins are [0,10,20,30,40,50,60]. 
# Create a histogram with x-axis label as "emplyee ages" and yaxis label as " no. of employees". 
# Create a title of the plot as "Oracle Corp". 
# Also teh color of histogram created should be cyan

import matplotlib.pyplot as pit

emp_ages = [22,45,30,59,58,56,57,45,43,43,50,40,34,33,25,19]
bins = [0,10,20,30,40,50,60]

pit.hist(emp_ages,bins=bins,color="Cyan")

pit.xlabel("Emplyee Ages")
pit.ylabel("No of Employees")
pit.title("Oracle Corp")

pit.show()