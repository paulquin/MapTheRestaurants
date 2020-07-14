import pandas as pd
import FindTheDetails as gcode

df = pd.read_csv("restaurant_list.csv", header = 0)

name_list = df['Name'].tolist()
address_list = []
lat_list = []
lng_list = []

for name in name_list:
	address_list.append(gcode.addressME(name))
	lat_list.append(gcode.latME(name))
	lng_list.append(gcode.lngME(name))

df2 = pd.DataFrame({'Name': name_list, 'Address' : address_list, 'Lat' : lat_list, 'Lng' : lng_list})

df2.to_csv('restaurants.csv', index = False)

