import pandas as pd
import folium
from folium.plugins import MarkerCluster

df = pd.read_csv("Aerodromes.csv")

# Convert coordinates to numeric
df['latitude_deg'] = pd.to_numeric(df['latitude_deg'], errors='coerce')
df['longitude_deg'] = pd.to_numeric(df['longitude_deg'], errors='coerce')

# Fill missing elevations
df['elevation_ft'] = pd.to_numeric(df['elevation_ft'], errors='coerce').fillna(0)

# Create heliport flag
df['is_heliport'] = df['type'].apply(lambda x: 1 if 'heliport' in x.lower() else 0)

# Center map on Nepal
nepal_map = folium.Map(location=[28.0, 84.0], zoom_start=7)

#Add airports to map
for idx, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude_deg'], row['longitude_deg']],
        radius=6,
        popup=(
            f"<b>{row['name']}</b><br>"
            f"Type: {row['type']}<br>"
            f"Elevation: {row['elevation_ft']} ft<br>"
            f"Score: {row['score']}"
        ),
        color='blue' if row['is_heliport']==0 else 'green',
        fill=True,
        fill_opacity=0.7
    ).add_to(nepal_map)

#Add layer Control
folium.LayerControl().add_to(nepal_map)

#save map as HTML
nepal_map.save("nepal_airports_map.html")

#cluster marker
from folium.plugins import MarkerCluster

cluster = MarkerCluster().add_to(nepal_map)

for idx, row in df.iterrows():
    folium.Marker(
        location=[row['latitude_deg'], row['longitude_deg']],
        popup=f"{row['name']} ({row['type']})"
    ).add_to(cluster)

#color code by elevation
for idx, row in df.iterrows():
    color = 'red' if row['elevation_ft'] > 7000 else 'orange' if row['elevation_ft'] > 3000 else 'blue'
    folium.CircleMarker(
        location=[row['latitude_deg'], row['longitude_deg']],
        radius=6,
        popup=f"{row['name']} ({row['type']})",
        color=color,
        fill=True,
        fill_opacity=0.7
    ).add_to(nepal_map)

folium.LayerControl().add_to(nepal_map)
