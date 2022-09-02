import folium

latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")
name = input("Enter marker name: ")
file = input("Save file as: ")
map = folium.Map(location=[40.75, -74.125])

marker = folium.Marker([latitude, longitude], popup=name)
marker.add_to(map)
map.save(outfile=file)