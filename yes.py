import folium
import pandas as pd

out = str(input("Enter output file: "))

def obtain_data():
    file = input("Enter a CSV file:")
    df = pd.read_csv(file)
    return df

def create_map():
    fol_map = folium.Map(location=[40.75, -74.125])
    return fol_map

def obtain_locations(df):
    locations = df.values.tolist()
    return locations

    create_map()
    create_marker(locations[0], locations[1])

def create_marker(latitude, longitude):
    newMarker = folium.Marker([latitude, longitude])
    newMarker.add_to(fol_map)

def save_map(map):
    map.save(outfile=map)

save_map(out)