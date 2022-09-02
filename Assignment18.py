#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np

boxes = int(input("Enter a size: "))
img = np.ones((boxes,boxes,3))

plt.grid()

img[0:boxes+1:2,0:boxes+1,0] = 1.0

plt.grid()

out = input("Enter output file name: ")
plt.imsave(out, img)
