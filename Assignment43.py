#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import folium
import pandas as pd

file = str(input("Enter CSV file name: "))

csv = pd.read_csv(file)
map = folium.Map(location=[40.768731, -73.964915])

for index,row in csv.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(map)

out = str(input("Enter output file: "))
map.save(outfile=out)