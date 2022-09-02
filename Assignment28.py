#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import pandas as pd

borough = input("Enter borough: ")

chart = pd.read_csv("nycHistPop.csv", skiprows=5)
chart.plot(x="Year")

print("Average Population:", chart[borough].mean())
print("Maximum Population:", chart[borough].max())