  
import requests
import json
import numpy as np
import matplotlib.pyplot as plt
import cv2

GOOGLE_KEY = "AIzaSyCqo0_1Yl5HXfELsH50WtVEdH0yUOlJe40"

def find_place(inp, inputtype, latitude, longditude):
    req = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=%s&inputtype=%s&locationbias=point:%f,%f&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=%s" % (inp, inputtype, latitude, longditude, GOOGLE_KEY))
    res = req.json()
    return res

def place_by_id(placeId):
    req = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid=%s&key=%s" % (placeId, GOOGLE_KEY))
    res = req.json()
    return res

def get_static_map(latitude, longditude, zoom, size, maptype):
    URL = "https://maps.googleapis.com/maps/api/staticmap?center=%f,%f&zoom=%i&size=%s&maptype=%s&format=jpg&markers=color:blue|label:G|%f,%f&key=%s" % (latitude, longditude, zoom, size, maptype, latitude, longditude, GOOGLE_KEY)
    print(URL)
    req = requests.get(URL)
    # resp = req.raw
    # image = np.asarray(bytearray(resp.read()), dtype="uint8")
    # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return req.content

def get_map_from_approx(inp, inputtype, latitude, longditude, zoom, size, maptype):
    place = find_place(inp, inputtype, latitude, longditude)
    place_lng = place["candidates"][0]["geometry"]["location"]['lng']
    place_lat = place["candidates"][0]["geometry"]["location"]['lat']
    # print("Request")
    # print("%f,%f" % (latitude, longditude))
    # print("%f,%f" % (place_lat, place_lng))

    Map = get_static_map(place_lat, place_lng, zoom, size, maptype)
    return Map




if __name__ == "__main__":
    # #place = find_place("Gas", "textquery", 33.1502061, -96.8978388)
    # # read and parse coordinates
    # place["candidates"][0]["geometry"]["location"]['lng']
    coords = np.genfromtxt('data/coords/100_coords.csv',delimiter = ",")
    # print(coords[1:, 2:].shape)
    coords = coords[1:, 2:]





    # # #loop through coords and get images
    mode = "satellite"
    zoom = 19
    mapsize = "600x600"
    for coord in coords: 
        Map = get_map_from_approx("Gas", "textquery", coord[0], coord[1], zoom, mapsize, mode)
        with open('data/images/%s_marked/%f_%f_%i_%s_approx.png' % (mode,coord[0], coord[1], zoom, mapsize), 'wb') as file:
            file.write(Map)
   
    # # Loop thorugh each coord and get image
    # mode = "satellite"
    # zoom = 19
    # map_size = "600x600"
    # for coord in coords:
    #     img = get_static_map(coord[0], coord[1], zoom, map_size, mode)
    #     with open('data/images/%s/new%f_%f_%i_%s.png' % (mode, coord[0], coord[1], zoom, map_size), 'wb') as file:
    #         file.write(img)


    # # Map = get_static_map(33.1502061, -96.8978388, 19, "600x300", "roadmap")
    # # with open('data/%f_%f.png', 'wb') as file:
    # #     file.write(Map)