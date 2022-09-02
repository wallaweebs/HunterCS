#Name: Debasree Sen
#Email: debasree.sen63@myhunter.cuny.edu

import folium

map = folium.Map(location=[40.75, -74.125], zoom_start=5)

folium.Marker(location=[40.768731, -73.964915], popup="Hunter College").add_to(map)

map.save(outfile="nycMap.html")