# Prayatna sells designer bags and wallets. During the sales season, he gave discounts
# ranging from 10% to 50% over a period of 5 weeks. He recorded his sales for each
# type of discount in an array. Draw a scatter plot to show a relationship between the
# discount offered and sales made. Take 5 sales in Rupees as user defined values

import matplotlib.pyplot as pit 
import numpy as np

x = np.array([10,20,30,40,50])
y = np.array([25000,61000,79100,65630,45200])

pit.xlabel('Discount Offered (%)')
pit.ylabel('Sales (Rupees)')
pit.title('Relationship between Discount Offered and Sales')

pit.scatter(x,y)

pit.show()