#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

borough = str(input("Enter borough name: "))
outpt = str(input("Enter output file name: "))

chart = pd.read_csv("nycHistPop.csv", skiprows=5)

chart["Fraction"] = chart[borough]/chart["Total"]
chart.plot(x="Year", y="Fraction")

figure = plt.gcf()
figure.savefig(outpt)