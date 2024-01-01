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
    df = data[['Latitude', 'Longitude']]

    # Remove duplicates
    df = df.drop_duplicates()

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
    
    # Get points
    x = np.array(df['Longitude'])
    y = np.array(df['Latitude'])

    # Manipulate img
    img = image.imread('map7.png')
    fig, ax = plt.subplots()
    
    # Set img boundaries
    ax.imshow(img, extent=[minLong, maxLong, minLat, maxLat])

    # Plot Graph
    plt.plot(x, y,  'o')
    plt.xlim(minLong, maxLong)
    plt.ylim(minLat, maxLat)

    plt.show()

df = pd.read_csv('GrowLocations.csv')
df = cleanData(df)
plotGraph(df)

