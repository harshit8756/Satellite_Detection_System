# website link :- https://view.genial.ly/6572be88c3e2fc00143a5590/interactive-content-iss-international-space-station
# git hub link :- 
# live location ISS :- https://www.orbtrack.org/#/?satName=ISS%20(ZARYA)


# json convert the python dictionary 
# above into a json
import json 
import turtle

# urllib.request fetch URLs using
# a variety of different protocols
import urllib.request 
import time 

# webbrowser provides a high-level interface
# to allow displaying Web-based documents 
# to users
import webbrowser 

# geocoder takes the data and locate these
# locations in the map
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url) 
result = json.loads(response.read())
file = open("iss.txt", "w") 

file.write("There are currently " +
			# prints number of astronauts
		str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]

# prints names of crew 
for p in people:
	file.write(p['name'] + " - on board" + "\n") 

# print long and lat

g = geocoder.ip('me') 
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")



# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)



# load the world map image
screen.bgpic("Satellite Detection/images/map.gif")
screen.register_shape("Satellite Detection/images\iss.gif")
iss = turtle.Turtle()
iss.shape("Satellite Detection/images\iss.gif")
iss.setheading(45)
iss.penup()


while True:

	# load the current status of the ISS in real-time
	url = "http://api.open-notify.org/iss-now.json"
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())

	# Extract the ISS location
	location = result["iss_position"]
	lat = location['latitude']
	lon = location['longitude']

	# Ouput lon and lat to the terminal
	lat = float(lat)
	lon = float(lon)
	print("\nLatitude: " + str(lat))
	print("\nLongitude: " + str(lon))

	# Update the ISS location on the map
	iss.goto(lon, lat)

	# Refresh each 1 seconds
	time.sleep(1)
