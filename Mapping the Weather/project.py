from requests import get    # for fetching data
import json                 # for processing JSON data
import folium               # for visualising data on maps
import os
import webbrowser
import html

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

stations = get(url).json()

longitudes = [station['weather_stn_long'] for station in stations['items']]
latitudes = [station['weather_stn_lat'] for station in stations['items']]
weatherStationNames = [html.escape(station['weather_stn_name']) for station in stations['items']]

# set up map
Default = [0,0]
UK = [54,-2]
US = [39.381266, -97.92211]
China = [35.86166, 104.195397]

map_ws = folium.Map(location=[0,0],zoom_start=3)

# add locations of all the weather stations
for n in range(len(longitudes)):
    folium.Marker([latitudes[n],
                longitudes[n]],
                icon = folium.Icon(icon = 'cloud', color = 'green'),
                popup = weatherStationNames[n]).add_to(map_ws)

# get current working directory
CWD = os.getcwd()
# save map as local html file
map_ws.save('wsmap1.html')
# open using browser
webbrowser.open_new('file://'+CWD+'/'+'wsmap1.html')