#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import matplotlib.pyplot as plt

inpt = str(input("Enter image: "))
output = str(input("File output name: "))

img = plt.imread(inpt)

height = img.shape[0]
width = img.shape[1]
img2 = img[height//2:, :width//2]

plt.imsave(output, img2)