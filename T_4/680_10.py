# Jeff is a branch manager at a local bank. Recently Jeffs is receiving customer feedback
# saying that the wait times for a client to be served by a customer service
# representative are too long. Jeff decides to observe and write down the time spent by
# each customer on waiting. Here are his findings from observing and writing down the
# wait times spent by 20 customers 
# (in seconds): 43.1, 35.6,37.6,36.5,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3,31.4,35.6,45.2,54.1,45.6,36.5,43.1
# Plot a histogram for the above data. Calculate bins and bins width and plot with
# calculated bins.

import matplotlib.pyplot as pit 

wait_times = [43.1, 35.6, 37.6, 36.5, 45.3, 43.5, 40.3, 50.2, 47.3, 31.2, 
              42.2, 45.5, 30.3, 31.4, 35.6, 45.2, 54.1, 45.6, 36.5, 43.1]

num_bin = 5
 
bin_whith = ( max(wait_times) - min(wait_times)) / num_bin
 
pit.hist(wait_times, bins=num_bin, color="Cyan")

pit.title("Wait Time Histogram")
pit.xlabel("Wait Time (seconds)")
pit.ylabel("Number of Customers")

pit.show()