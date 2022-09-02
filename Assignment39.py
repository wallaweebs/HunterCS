#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import pandas as pd

data = input("Enter CSV file name: ")
file = pd.read_csv(data)
print("Top three contributing factors for collisions:")
print(file["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])