import requests
import googlemaps
import time
import os 
import random


class restaurantChooser():
    def __init__(self, searchLocation, searchWord, radius = 3):
        self.location = searchLocation
        self.rawRadius = int(radius)
        self.keyword = searchWord
        self.radius = ""
        self.API_KEY = os.environ.get("API_KEY")
        self.gmaps = googlemaps.Client(key=self.API_KEY)
        self.latlng = ""
        self.chosen = ""
        
    def getRadius(self):

        #Limits and Sets Radius
        #Converts miles into meters for the calcuation purposes
        
        if self.rawRadius > 100:
            self.rawRadius = 100
        elif self.rawRadius < 0:
            self.rawRadius = .5
        self.radius = str(self.rawRadius * 1609.34)

    def getLatLng(self):
        geoCodeURL = "https://maps.googleapis.com/maps/api/geocode/json?address=" + self.location + "&key=" + self.API_KEY
        response = requests.get(geoCodeURL).json()
        response.keys()
        if response['status'] == 'OK':
            geometry = response['results'][0]['geometry']
            self.latlng = str(geometry['location']['lat']) +"%2C" + str(geometry['location']['lng'])

    def searchNearby(self):
        searchURL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + self.latlng + "&radius=" + self.radius + "&type=restaurant&keyword=" + self.keyword + "&key=" + self.API_KEY
        response = requests.get(searchURL).json()
        response.keys()
        if response['status'] == 'OK':
            seedRange = len(response['results']) - 1
            seed = random.randint(0,seedRange)
            self.chosen = response['results'][seed]

    def run(self):
        # Runs each function to create the result
        # Adds a slight delay to throttle usage
        self.getRadius()
        time.sleep(1)
        self.getLatLng()
        time.sleep(1)
        self.searchNearby()
        

