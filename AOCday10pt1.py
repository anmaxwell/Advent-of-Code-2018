import numpy as np
import matplotlib.pyplot as plt
import re

with open('/Users/aniamaxwell/adventofcode/input/day10input.txt', 'r') as myfile:
    filecntent = myfile.readlines()

coords = []
velocity = []

for item in filecntent:
    result = re.findall(r"[-+]\d+|\d+", item)
    coords.append([int(result[0]), int(result[1])])
    velocity.append([int(result[2]), int(result[3])])

def moveStars(coords):
    starlist = []
    for i in range(len(coords)):
        position = (np.array(coords[i]) + np.array(velocity[i]))
        starlist.append(list(position))
        coords[i] = starlist[i]
    return starlist, coords


for i in range(10000):
    starlist, coords = moveStars((coords))

data = np.array([starlist])
x, y = data.T
plt.scatter(x,y, marker='*')
plt.show()
