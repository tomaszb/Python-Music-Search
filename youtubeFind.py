import gdata.youtube
import gdata.youtube.service
import gdata.alt.appengine


def searchandAdd(playlist, artist, songname):
	client = gdata.youtube.service.YouTubeService()
	gdata.alt.appengine.run_on_ appengine(client)
	query = gdata.youtube.service.YouTubeVideoQuery()

	query.vq = artist + ' ' + songname
	query.orderby = 'viewCount'
	query.max_results = '1'

	feed = client.YouTubeQuery(query)


