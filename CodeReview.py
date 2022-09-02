import matplotlib.pyplot as plt
import numpy as np

grid = np.ones((50, 50, 3))

grid[0:31, 0:11, 1] = 0
grid[0:51, 40:51, 1] = 0
grid[20:31, 0:51, 1] = 0


grid[0:31, 0:11, 0] = 0
grid[0:51, 40:51, 0] = 0
grid[20:31, 0:51, 0] = 0

plt.imshow(grid)
plt.show()