import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

print(df)

# Filter lat and lang based on min and max values
df = df[(df['Latitude'] >= minLat) & (df['Latitude'] <= maxLat) & (df['Longitude'] >= minLong) & (df['Longitude'] <= maxLong)]


x = np.array(df['Longitude'])
y = np.array(df['Latitude'])

plt.plot(x, y,  'o')
plt.xlim(minLong, maxLong)
plt.ylim(minLat, maxLat)

plt.show()

# data = []

# for line in file:
    
#     x = line.split(',')
#     data.append(x[:4])

   
# for x in data[:10]: 
#     print(x)
    
    
    # for x in new_df.index:
#     try:
#         lat = new_df.loc[x, 'Latitude']
#         long = new_df.loc[x, 'Longitude']
        
#         if not (minLat <= lat <= maxLat and minLong <= long <= minLong):
#             df.drop(x, inplace = True)
            
#     except Exception as e:
#         df.drop(x, inplace = True) 


# cleanData = []

# for x in data[2:]: 

#     try:
#         lat = float(x[1])
#         long = float(x[2])
        
#         if minLat <= lat <= maxLat and minLong <= long <= minLong:
#             cleanData.append(x)
            
#     except Exception as e:
#         pass 
        
    

            
# for x in data: 
#     print(x)