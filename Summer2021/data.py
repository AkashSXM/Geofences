import requests
import numpy as np
import matplotlib.pyplot as plt

GOOGLE_KEY = "AIzaSyCqo0_1Yl5HXfELsH50WtVEdH0yUOlJe40"

def find_place(inp, inputtype, latitude, longditude):
    req = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=%s&inputtype=%s&locationbias=point:%f,%f&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=%s" % (inp, inputtype, latidude, longditudeGOOGLE_KEY))
    return req

def place_by_id(placeId):
    req = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid=%s&key=%s" % (placeId, GOOGLE_KEY))
    return req

def get_static_map(latitude, longditude, zoom, size, maptype):
    req = requests.get("https://maps.googleapis.com/maps/api/staticmap?center=%f,%f&zoom=%f&size=%s&maptype=%s&key=%s" % (GOOGLE_KEY))
    return req

if __name__ == "__main__":
    res = find_place("Gas", "textquery", 33.1502061, -96.8978388)
    