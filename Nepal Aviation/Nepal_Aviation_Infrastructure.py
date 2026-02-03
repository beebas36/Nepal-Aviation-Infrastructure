import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Aerodromes.csv')
df.head()
df.info()
df.describe(include='all')
df.isnull().sum()

#Data Cleaning
#Converting string to numeric
df['latitude_deg'] = pd.to_numeric(df['latitude_deg'], errors='coerce')
df['longitude_deg'] = pd.to_numeric(df['longitude_deg'], errors='coerce')
df['elevation_ft'] = pd.to_numeric(df['elevation_ft'], errors='coerce')

#Handling Missing values
df['elevation_ft'].fillna(df['elevation_ft'].mean(), inplace=True)
df.drop_duplicates(inplace=True)

#create heliport flag
df['is_heliport'] = df['type'].apply(lambda x: 1 if 'heliport' in x.lower() else 0)

#create elevation category
def elevation_category(x):
    if x < 3000:
        return 'Low'
    elif 3000 <= x < 7000:
        return 'Medium'
    else:
        return 'High'
    
df['elevation_level'] = df['elevation_ft'].apply(elevation_category)

#Exploratory Data Analysis
#Airport type distribution
type_counts = df['type'].value_counts()
print(type_counts)

#plot
type_counts.plot(kind = 'bar')
plt.title("Airport by Type")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

#Region wise count
region_count = df['region_name'].value_counts()
print(region_count.head())

#plot
region_count.plot(kind='bar', figsize=(10,5))
plt.title("Airports by Region")
plt.xticks(rotation=45)
plt.show()

#Elevation Distribution
df['elevation_ft'].plot(kind='hist', bins=10)
plt.title("Elevation Distribution")
plt.xlabel("Elevation (ft)")
plt.show()

#KPI Calculation
total_airports = df.shape[0]
heliports = df['is_heliport'].sum()
avg_elevation = df['elevation_ft'].mean()
max_elevation = df['elevation_ft'].max()
min_elevation = df['elevation_ft'].min()

print("Total Airports:", total_airports)
print("Total Heliports:", heliports)
print("Average Elevation:", round(avg_elevation,2))
print("Highest Elevation:", max_elevation)
print("Lowest Elevation:", min_elevation)

#Top airport by elevation
df[['name','elevation_ft']].sort_values(by='elevation_ft', ascending=False).head()

#Top by score
df[['name','score']].sort_values(by='score', ascending=False).head()

#Geographic Visualization
plt.figure(figsize=(8,6))
plt.scatter(df['longitude_deg'], df['latitude_deg'])
plt.title("Geographic Distribution of Airports in Nepal")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

df.groupby('elevation_level').size()

df.groupby('type')['elevation_ft'].mean()