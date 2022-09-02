#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

file = input("Enter name of input file: ")
output = input("Enter name of output file:")
chart = pd.read_csv(file, skiprows=0)

chart["Fraction Children"] = chart["Total Children in Shelter"]/chart["Total Individuals in Shelter"]
chart.plot(x="Date of Census", y="Fraction Children")

figure = plt.gcf()
figure.savefig(output)