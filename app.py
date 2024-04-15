from flask import Flask, jsonify, request
import googlemaps  # This line only needed if you use the googlemaps library
from datetime import datetime
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all domains on all routes. Consider tightening this for production!

def get_route(origin, destination, mode, key):
    """
    Fetches route using the Google Maps Directions API.
    :param origin: Starting point address as a string.
    :param destination: Destination address as a string.
    :param mode: Mode of transport ('driving', 'walking', 'bicycling', 'transit').
    :param key: Your Google Maps API key.
    :return: JSON response with route details.
    """
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        'origin': origin,
        'destination': destination,
        'mode': mode,
        'key': key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'error', 'message': 'Failed to retrieve directions'}

@app.route('/get-itinerary')
def get_itinerary():
    destinations = [
        "Navy Pier, Chicago, IL",
        "Lincoln Park Zoo, Chicago, IL",
        "The Plant Chicago, Chicago, IL",
        "Green Street Smoothie Co, Chicago, IL"
    ]
    origin = "171 W Randolph St, Chicago, IL"
    mode = 'driving'
    api_key = 'AIzaSyCTMf0bJ6YHbUn-q91uJYUGO5ReVOxQKCM'  # Replace with your actual Google Maps API key
    routes = []

    for destination in destinations:
        route_info = get_route(origin, destination, mode, api_key)
        if route_info and route_info.get('status') == 'OK':
            routes.append(route_info)
        else:
            routes.append({'status': 'error', 'message': 'Failed to retrieve directions to ' + destination})
        origin = destination  # Set the current destination as the new origin for the next trip

    return jsonify(routes)

if __name__ == '__main__':
    app.run(debug=True)
