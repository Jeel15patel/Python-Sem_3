# Consider that a survey has to be done on how much distance the following vehicles
# have covered in a span of five days. The data collected can be plotted in different
# plotting methods. Draw a scatter plot by considering following style properties.
# (a)Consider red colour for ENFIELD, blue colour for HONDA, yellow colour for
# YAMAHA and black colour for KTM.
# (b)Add label for each bike details.
# (c)Add x and y label, x label should be named as ‘Days’ and y label should be named as‘Distance in kms’.
# (d)Add a Ɵtle named ‘Bike details in scaƩer plot’.
# (e)Add legends at the upper right corner
# Data From QB

import matplotlib.pyplot as pit 
import numpy as np

x = np.array([1,2,3,4,5])

y1 = np.array([50,40,70,80,20])
y2 = np.array([80,20,20,50,60])
y3 = np.array([70,20,60,40,60])
y4 = np.array([80,20,20,50,60])

pit.scatter(x,y1,label="ENFIELD",color="Red")
pit.scatter(x,y2,label="HONDA",color="Blue")
pit.scatter(x,y3,label="YAMAHA",color="Yellow")
pit.scatter(x,y4,label="KTM",color="Black")

pit.xlabel("Days")
pit.ylabel("Distance in kms")
pit.title("Bike details in scatter plot")

pit.legend()

pit.show()
