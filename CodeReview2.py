import matplotlib.pyplot as plt
import pandas as pd

borough = input("Enter a borough: ")

file = pd.read_csv("covidCases.csv")
file.plot(x="Date of Interest", y=borough)

plt.show()

print("Minimum: ", file[borough].min())
print("Maximum: ", file[borough].max())
print("Mean: ", file[borough].mean())
print("Median: ", file[borough].median())
print("Standard Deviation: ", file[borough].std())


