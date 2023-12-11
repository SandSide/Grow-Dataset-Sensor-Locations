import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as image
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)

df = pd.read_csv('GrowLocations.csv')

# Ranges
minLong= -10.592
maxLong = 1.6848

minLat = 50.681
maxLat = 57.985

relevant_data = []

# Story only relevant data
df = df[['Latitude', 'Longitude']]

# Remove duplicates
df = df.drop_duplicates()

# Switch columns to correct place
df = df.rename(columns={'Latitude': 'temp', 'Longitude': 'Latitude'})
df = df.rename(columns={'temp': 'Longitude'})

# Filter lat and lang based on min and max values
df = df[(df['Latitude'] >= minLat) & (df['Latitude'] <= maxLat) & (df['Longitude'] >= minLong) & (df['Longitude'] <= maxLong)]

# Plot graph
x = np.array(df['Longitude'])
y = np.array(df['Latitude'])

img = image.imread('map7.png')

fig, ax = plt.subplots()
ax.imshow(img, extent=[minLong, maxLong, minLat, maxLat])

plt.plot(x, y,  'o')
plt.xlim(minLong, maxLong)
plt.ylim(minLat, maxLat)

plt.show()