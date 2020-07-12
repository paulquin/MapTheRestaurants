import requests
import urllib.parse



#text search
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
apikey = 'YOUR API KEY'

def placeidME(location):
	location = urllib.parse.quote(str(location) + ' Greater Vancouver')
	
	req = 'query={}&key={}'.format(location,apikey)
	request = url + req
	result = requests.get(request)
	data = result.json()
	
	place_id = data['results'][0]['place_id']


	return place_id

print(placeidME("I&I Jamaican Restaurant"))

