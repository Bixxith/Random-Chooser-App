import requests
import googlemaps
from datetime import datetime
import time
import json
import os

API_KEY = os.environ.get("API_KEY")

searchLocation = 'Rockville, Indiana'
searchWord= "Taco"
radius = "1500"
gmaps = googlemaps.Client(key=API_KEY)
base_url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + searchLocation + "&key=" + API_KEY 
response = requests.get(base_url).json()

response.keys()
time.sleep(1)
if response['status'] == 'OK':
    geometry = response['results'][0]['geometry']
    latlng = str(geometry['location']['lat']) +"%2C" + str(geometry['location']['lng'])


searchURL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + latlng + "&radius=" + radius + "&type=restaurant&keyword=" + searchWord + "&key=" + API_KEY


testResponse = requests.get(searchURL).json()

print(testResponse['results'][0]['name'])
