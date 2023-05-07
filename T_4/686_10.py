# Consider that a survey has to be done on income and saving of each month for seven
# different persons. The data collected can be plotted in different plotting methods.
# Draw a scatter plot by considering following style properties.
# (a)Consider red colour for “High income low saving” and blue colour for “Low income high saving”
# (b)Add label for each field i.e. “High income low saving” and “low income high saving” details.
# (c)Add x and y label, x label should be named as ‘SAVINGS (in hundreds)’ and y label should be named as ‘INCOME (in thousands)’.
# (d)Add a Ɵtle named ‘Income v/s salary scaƩer plot’.
# (e)Add legends at the upper right corner.
# Data From QB

import matplotlib.pyplot as pit 
import numpy as np

HILS_x = np.array([100,150,200,250,300,350,360])
HILS_y = np.array([7500,8000,8500,9000,9500,10000,10500])

LIHS_x = np.array([800,850,900,950,100,105,110])
LIHS_x = np.array([3000,3500,3700,4000,4500,5000,5200])

pit.scatter(HILS_x,HILS_y,label="High Income Low Saving",color="Red")

pit.scatter(LIHS_x,LIHS_x,label="Low Income High Saving",color="Blue")

pit.legend()

pit.xlabel("SAVINGS (in hundreds)")
pit.ylabel("INCOME (in thousands)")
pit.title("Income v/s salary scatter plot")

pit.show()