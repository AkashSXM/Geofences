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
    URL = "https://maps.googleapis.com/maps/api/staticmap?center=%f,%f&zoom=%i&size=%s&maptype=%s&format=jpg&key=%s" % (latitude, longditude, zoom, size, maptype, GOOGLE_KEY)
    print(URL)
    req = requests.get(URL)
    # resp = req.raw
    # image = np.asarray(bytearray(resp.read()), dtype="uint8")
    # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return req.content

if __name__ == "__main__":
    place = find_place("Gas", "textquery", 33.1502061, -96.8978388)


    # Read and parse coordinates
    coords = np.genfromtxt("data/coords/100_coords.csv", delimiter=",")
    print(coords[1:, 2:].shape)
    coords = coords[1:, 2:]

    # Loop thorugh each coord and get image
    mode = "satellite"
    zoom = 18
    map_size = "600x600"
    for coord in coords:
        img = get_static_map(coord[0], coord[1], zoom, map_size, mode)
        with open('data/images/%s/%f_%f_%i_%s.png' % (mode, coord[0], coord[1], zoom, map_size), 'wb') as file:
            file.write(img)


    # Map = get_static_map(33.1502061, -96.8978388, 19, "600x300", "roadmap")
    # with open('data/%f_%f.png', 'wb') as file:
    #     file.write(Map)

    # https://maps.googleapis.com/maps/api/staticmap?center=33.150206,-96.897839&zoom=19.000000&size=600x300&maptype=roadmap&format=jpg&key=AIzaSyCqo0_1Yl5HXfELsH50WtVEdH0yUOlJe40
    # https://maps.googleapis.com/maps/api/staticmap?center=33.1502061,-96.8978388&zoom=19&size=600x300&maptype=roadmap&key=AIzaSyCqo0_1Yl5HXfELsH50WtVEdH0yUOlJe40
    # Map = requests.get("https://maps.googleapis.com/maps/api/staticmap?center=33.1502061,-96.8978388&zoom=19&size=600x300&maptype=roadmap&key=AIzaSyCqo0_1Yl5HXfELsH50WtVEdH0yUOlJe40")
    # with open('mapTest.png', 'wb') as file:
    #     file.write(Map.content)