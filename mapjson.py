import urllib.request, json
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'API_KEY'
origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
#print(directions)
#Extracting json data
#the syntax is: mydict[key] = "value"
routes=directions['routes']
bounds=routes[0]
legs=bounds['legs']
legger=legs[0]
durationlist=legger['duration']
distancelist=legger['distance']
distancestr=distancelist['text']
durationstr=durationlist['text']
distancem=distancestr.split()
distance=distancem[0]
#durationstr='9 hours 2 mins'
l=durationstr.split()
hour=l[0]
minute=l[2]
print(hour,":",minute,"\n",distance)
