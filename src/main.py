import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as image
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)

# Ranges
minLong= -10.592
maxLong = 1.6848

minLat = 50.681
maxLat = 57.985

def cleanData(data):
    """ Clean the data inside the data frame

    Args:
        data (data frame): Data frame to clean

    Returns:
        data frame: Cleaned data frame
    """

    # Story only relevant data
    df = data[['Latitude', 'Longitude', 'Type']]

    # Remove duplicates
    df = df.drop_duplicates()
    
    # Keep only type of sensor
    df['Type'] = df['Type'].apply(lambda x: x.rsplit('.', 1)[-1])
    
    # Switch columns names to correct place
    df = df.rename(columns={'Latitude': 'temp', 'Longitude': 'Latitude'})
    df = df.rename(columns={'temp': 'Longitude'})

    # Filter lat and lang based on min and max values
    df = df[(df['Latitude'] >= minLat) & (df['Latitude'] <= maxLat) & (df['Longitude'] >= minLong) & (df['Longitude'] <= maxLong)]
    
    return df

def plotGraph(data):
    """Plot data onto a graph

    Args:
        data (data frame): Data to plot
    """
    
    colors = {'AirTemperature':'red', 'FertilizerLevel':'green', 'SoilMoisture':'blue', 'Light':'yellow', 'BatteryLevel':'orange', 'WaterTankLevel':'black'}
    
    # Get points
    x = np.array(df['Longitude'])
    y = np.array(df['Latitude'])
    col = df['Type'].map(colors)

    # Manipulate img
    img = image.imread('map7.png')
    fig, ax = plt.subplots()
    
    # Set img boundaries
    ax.imshow(img, extent=[minLong, maxLong, minLat, maxLat])
    
    grouped = df.groupby('Type')
    for key, group in grouped:
        group.plot(ax=ax, kind='scatter', x='Longitude', y='Latitude', label=key, color=colors[key])

    # # Plot Graph
    # plt.scatter(x, y)
    # plt.xlim(minLong, maxLong)
    # plt.ylim(minLat, maxLat)
    # plt.title('Growth Sensors in UK')
    # plt.xlabel('Longitude')
    # plt.ylabel('Latitude')

    plt.show()


df = pd.read_csv('GrowLocations.csv')
df = cleanData(df)
print(df)
plotGraph(df)

