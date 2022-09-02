#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import pandas as pd

name = input("Enter file name: ")
attribute = input("Enter attribute: ")

file = pd.read_csv(name)
print("The 10 worst offenders are:")
print(file[attribute].value_counts()[:10])
