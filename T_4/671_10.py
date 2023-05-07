# These cost categories applied to a $9.00 microcontroller:
# Engineering $1.35
# Manufacturing $3.60
# Sales $2.25
# Profit $1.80
# Create a pie chart will show the cost breakdown as different sized pieces.

import matplotlib.pyplot as plt

categories = ['Engineering', 'Manufacturing', 'Sales', 'Profit']
costs = [1.35, 3.60, 2.25, 1.80]
total_cost = sum(costs)
percentages = [cost / total_cost * 100 for cost in costs]

plt.pie(percentages, labels=categories, autopct='%1.1f%%')
plt.title('Cost Breakdown of a $9.00 Microcontroller')

plt.show()