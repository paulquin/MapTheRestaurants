import requests
import urllib.parse

url = 'https://maps.googleapis.com/maps/api/'

#Replace it with your Google API Key
apikey = 'YOUR API KEY'

#Change to your target city and country
city = ',+Greater+Vancouver'
country = 'CA'

#geocode search for address
def addressME(location):
	location = str(location).replace(' ','+') + city
	query = 'geocode/json?address={}&key={}'.format(location,apikey)
	request = url + query
	result = requests.get(request)
	data = result.json()
	
	formatted_address = data['results'][0]['formatted_address']
	
	while True:
		try:
			if data['results'][0]['address_components'][-2]['short_name'] != country:
				return None
			else:
				return formatted_address
		except IndexError:
			return None

#text search for place ID
def placeidME(location):
	location = urllib.parse.quote(str(location) + city)
	
	req = 'place/textsearch/json?query={}&key={}'.format(location,apikey)
	request = url + req
	result = requests.get(request)
	data = result.json()
	
	place_id = data['results'][0]['place_id']

	return place_id

#text search for lat
def latME(location):
	location = urllib.parse.quote(str(location) + city)
	
	req = 'place/textsearch/json?query={}&key={}'.format(location,apikey)
	request = url + req
	result = requests.get(request)
	data = result.json()
	
	lat = data['results'][0]['geometry']['location']['lat']

	return lat

#text search for lng
def lngME(location):
	location = urllib.parse.quote(str(location) + city)
	
	req = 'place/textsearch/json?query={}&key={}'.format(location,apikey)
	request = url + req
	result = requests.get(request)
	data = result.json()
	
	lng = data['results'][0]['geometry']['location']['lng']
	
	return lng
