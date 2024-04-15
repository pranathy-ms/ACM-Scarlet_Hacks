hugging_face.py - uses the mistral model in hugging_face to generate an itinerary
app.py - python flask module that communicates with the angular front end and receives the request; processes by invoking Google Maps API, after receiving the itinerary from hugging face
angular project - UI to communicate and tackle the problem
