from geopy.geocoders import Nominatim
import pandas as pd

df = pd.read_csv('file_storage/country_list.csv')

address = df['Address'].tolist()

# create coordinate lists 
y = []
x = []
detail = []

# start geocoding 
geolocator = Nominatim(user_agent="batch-geocode")

# loop through each address 
for address in address:
    location = geolocator.geocode(address)
    # append results 
    y_coord = y.append(location.latitude)
    x_coord = x.append(location.longitude)
    # detail.append.location.raw

# test result 
print(y_coord)