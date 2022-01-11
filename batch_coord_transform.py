from pyproj import Transformer
import pandas as pd

df = pd.read_csv('file_storage/coordinates.csv')
y_list = df['Y'].tolist() # Lat
x_list = df['X'].tolist() # Lon 

# define transformation CRS 
transformer = Transformer.from_crs(4326, 20936)

# create result list
y_coords = []
x_coords = []

# Loop through lists
for y, x in zip(y_list, x_list):
    trans_coords = transformer.transform(y, x)
    # append to list
    y_coords.append(trans_coords[0])
    x_coords.append(trans_coords[1])

# create dictionary 
dict = {'Y': y_list,
        'X': x_list,
        'Y_Trans': y_coords,
        'X_Trans': x_coords,
    }

df_new =pd.DataFrame(dict)

# convert to CSV
df_new.to_csv('file_storage/converted_coordinates.csv')




