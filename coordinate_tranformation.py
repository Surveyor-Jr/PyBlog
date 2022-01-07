"""
Run package installation 

***
pip install pyproj 
***

"""

# Import the pyproj transfomation library
from pyproj import Transformer

# get the WKID of the Coordinate System (i.e. WGS84 => 4326)
transformer = Transformer.from_crs(4326, 20936)

# transform from 4326 => (to) => 20936
# 9053 => ARC 1950/UTM 36S

# Print the coordinates
print(transformer.transform(-17.835622, 31.044403))