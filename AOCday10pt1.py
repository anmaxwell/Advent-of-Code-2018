import numpy as np
import matplotlib.pyplot as plt
import re

a = np.array([3,9])
b = np.array([1,-2])

a=a+b
print(a)

list = ([3,9],[1, -2], [2,4])

data = np.array([list])
x, y = data.T
plt.scatter(x,y, marker='^')
plt.show()

with open('/Users/aniamaxwell/adventofcode/input/day10ainput.txt', 'r') as myfile:
    filecntent = myfile.readlines()

print(len(filecntent))
