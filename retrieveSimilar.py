import urllib, urllib2, urlparse
from Artist import *


APIKEY = "YETQALRUNYZDIOLCU"

def getEchoNestArtists(artist, listofartist, action):
	f = urllib.urlopen("http://developer.echonest.com/api/v4/artist/" + action + "?api_key=" + APIKEY + "&name=" + artist)
	response = f.read()

	result = similarParse(response, listofartist)

	return result

def similarParse(response, listofartist):
	results = []
	data = json.loads(response)
	print data
	artistslist = data["response"]["artists"]

	names =[]
	ids = []
	for one in artistslist:
		for key in one:
			if (key == "name"):
				names.append(str(one[key]))
			else:
				ids.append(str(one[key]))


	for x in range(0, len(names)):
		tempartist = Artist(names[x], ids[x])
		listofartist.append(tempartist)
		results.append(tempartist)
				
	return results
