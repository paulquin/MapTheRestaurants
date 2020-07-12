import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json?'
apikey = 'YOUR API KEY'

def gcode(location):
	location = str(location).replace(' ','+') + ',+Greater+Vancouver'
	query = 'address={}&key={}'.format(location,apikey)
	request = url + query
	result = requests.get(request)
	data = result.json()
	
	formatted_address = data['results'][0]['formatted_address']
	
	while True:
		try:
			if data['results'][0]['address_components'][-2]['short_name'] != 'CA':
				return None
			else:
				return formatted_address
		except IndexError:
			return None
	

#print(gcode("I&I Jamaican Restaurant"))

