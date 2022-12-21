# pp 143 
# to work out in Google Colab

!pip install -q condacolab
import condacolab
condacolab.install()

!mamba install -q -c conda-forge cartopy  

import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter  

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
calif_cities = us_cities[us_cities.State.eq('California')]
fig, ax = plt.subplots(figsize=(15,8))
ax = plt.axes(projection=ccrs.Mercator())
ax.coastlines('10m')
ax.set_yticks([35,36,37,38,39], crs=ccrs.PlateCarree())
ax.set_xticks([-125, -124, -123, -122, -121, -120, -119], crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter()
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
ax.set_extent([-125, -121, 35, 39])
ax.set_extent([-125, -121, 35, 39], crs=ccrs.PlateCarree())
X = calif_cities['lon']
Y = calif_cities['lat']
ax.scatter(X, Y, color='red', marker='o', transform=ccrs.PlateCarree())
plt.show()  
