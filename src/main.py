import numpy as np
import pandas as pd
import re
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
    
    # Switch columns names to correct place
    df = df.rename(columns={'Latitude': 'temp', 'Longitude': 'Latitude'})
    df = df.rename(columns={'temp': 'Longitude'})
    
    # Extract lat and long from Serial
    df_extracted = extractCoordsFromColumn(data['Serial'])
    
    # Append extracted coords
    df = pd.concat([df, df_extracted], ignore_index=True)
    
    # Remove duplicates
    df = df.drop_duplicates()

    # Filter lat and lang based on min and max values
    df = df[(df['Latitude'] >= minLat) & (df['Latitude'] <= maxLat) & (df['Longitude'] >= minLong) & (df['Longitude'] <= maxLong)]
    
    return df

def extractCoordsFromColumn(col):
    """Extract longitude and latitude from column if they exist in the string

    Args:
        col (Data frame column): Columns of strings to extract long and lat from

    Returns:
        data frame: Data frame of longitude and latitude
    """
    
    # Find cols which contain lat and long
    col = col[col.str.contains('Latitude', na=False) & col.str.contains('Longitude', na=False)]
    
    # Extract longs and lats
    lats = col.str.extract(r'Latitude:(\d+\.\d+)', expand=False)
    longs = col.str.extract(r'Longitude:(\d+\.\d+)', expand=False)
    
    df = pd.DataFrame({'Longitude': lats, 'Latitude': longs}).astype(float);
    
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
    plt.title('Growth Sensors in UK')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    plt.show()


df = pd.read_csv('GrowLocations.csv')
df = cleanData(df)
plotGraph(df)