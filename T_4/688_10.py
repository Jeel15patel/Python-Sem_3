# Plot a subplot showing the marks of 5 students for 6 subjects 
# Digital Electronics, Probability and Stochastics, Python, Full Stack Development, IELTS (Reading), and Data Structure). 
# All the marks for each subject and for each student is to be taken
# user defined. Subplot should be prepared for each subject. Each Subplot should have
# a title of subject along with a main title of a plot. 

# <------------------------------------------------------------------------------------->

import matplotlib.pyplot as pit
import numpy as np

x = np.array([1,2,3,4,5])

DE = eval(input("Enter Student Marks for Digital Electronics out of 25: "))
pit.subplot(2,3,1)
pit.title("Digital Electronics")
pit.scatter(x,DE,color="Red")

PS = eval(input("Enter Student Marks for Probability and Stochastics out of 25: "))
pit.subplot(2,3,2)
pit.title("Probability and Stochastics")
pit.scatter(x,PS,color="Green")

PY = eval(input("Enter Student Marks for Python out of 25: "))
pit.subplot(2,3,3)
pit.title("Python")
pit.scatter(x,PY,color="Yellow")

FSD = eval(input("Enter Student Marks for Full Stack Development out of 25: "))
pit.subplot(2,3,4)
pit.title("Full Stack Development")
pit.scatter(x,FSD,color="Blue")

IELTS = eval(input("Enter Student Marks for IELTS (Reading) out of 25: "))
pit.subplot(2,3,5)
pit.title("IELTS (Reading)")
pit.scatter(x,IELTS,color="Black")

DS = eval(input("Enter Student Marks for Data Structure out of 25: "))
pit.subplot(2,3,6)
pit.title("Data Structure")
pit.scatter(x,DS,color="Cyan")

pit.suptitle("6 Subject Marks")

pit.show()

# <------------------------------------------------------------------------------------->

#import matplotlib.pyplot as plt

# marks = {
#     'Digital Electronics': [70, 80, 60, 75, 90],
#     'Probability and Stochastics': [80, 85, 75, 70, 90],
#     'Python': [90, 85, 95, 80, 70],
#     'Full Stack Development': [70, 75, 80, 85, 90],
#     'IELTS (Reading)': [8, 7, 7.5, 8.5, 9],
#     'Data Structure': [85, 90, 80, 75, 95]
# }

# fig, axs = plt.subplots(2, 3, figsize=(12, 8))
# fig.suptitle('Marks for 6 Subjects', fontsize=16)

# for i, subject in enumerate(marks.keys()):
#     row = i // 3
#     col = i % 3
#     axs[row, col].bar(range(1, 6), marks[subject])
#     axs[row, col].set_title(subject)
#     axs[row, col].set_xlabel('Student')
#     axs[row, col].set_ylabel('Marks')

# plt.show()