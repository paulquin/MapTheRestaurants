import pandas as pd
import geopandas as gpd

restaurant_data = pd.read_csv('restaurants.csv')

restaurant_gdf = gpd.GeoDataFrame(restaurant_data, geometry = gpd.points_from_xy(restaurant_data['Lon'], restaurant_data['Lat']))

ESRI_WKT = ''

restaurant_gdf.to_file(filename = 'restaurants.shp', driver = 'ESRI Shapefile', crs_wkt = ESRI_WKT)
