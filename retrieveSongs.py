import json, pprint, urllib, urllib2, logging

APIKEY = "YETQALRUNYZDIOLCU"

def getEchoNestSongs(listofArtists):
	for everyArt in listofArtists:
		response = connectforSongs(everyArt.id)

		listofsongs = parseSongs(response)

		everyArt.addSongs(listofsongs)
def connectforSongs(Artist_id):
	f = urllib.urlopen("http://developer.echonest.com/api/v4/song/search?api_key=" + APIKEY + "&artist_id=" + Artist_id + "&sort=song_hotttnesss-desc&bucket=song_hotttnesss")
	response = f.read()

	return response

def parseSongs(response):
	data = json.loads(response)
	logging.debug(response)
	songslist = data["response"]["songs"]

	titles = []
	for one in songslist:
		for key in one:
			if (key == "title"):
				titles.append(one[key])

	return titles
