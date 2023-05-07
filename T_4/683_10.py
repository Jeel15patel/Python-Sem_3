# Create a Line Plot in which x points varies from 3 to 21. And the y points varies
# according to the equation y=2x+8. 

import matplotlib.pyplot as pit 

x = range(3,21)
y = [2*i+8 for i in x]

pit.plot(x,y)

pit.xlabel('x points')
pit.ylabel('y points')

pit.title('Line Plot')

pit.show()