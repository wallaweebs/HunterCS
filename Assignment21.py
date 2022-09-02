#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np
pic = str(input("Enter a file: "))
img = plt.imread(pic)
white = 0
x = 0.75

for i in range(img.shape[0]):
    for y in range(img.shape[1]):
        if(img[i,y,0] > x) and (img[i,y,1] > x) and (img[i,y,2] > x):
            white += 1

print("Snow count is", white)