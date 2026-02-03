# app.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("Nepal Aviation Infrastructure Dashboard")

# Load your dataset
df = pd.read_csv("Aerodromes.csv")  # replace with your dataset path

st.subheader("Data Preview")
st.dataframe(df.head())

st.subheader("Map of Airports/Heliports")

# Create a map
m = folium.Map(location=[28.3949, 84.1240], zoom_start=7)  # Nepal center

# Add markers from your dataset
for i, row in df.iterrows():
    folium.Marker(
        location=[row['latitude_deg'], row['longitude_deg']],
        popup=row['name']
    ).add_to(m)

# Display map in Streamlit
st_folium(m, width=700, height=500)
