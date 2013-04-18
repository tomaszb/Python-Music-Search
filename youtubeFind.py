import gdata.youtube
import gdata.youtube.service
import gdata.alt.appengine

import logging


def searchandAdd(artist, songname):
	listofterms = []
	listofterms.append(artist)
	for word in songname:
		listofterms.append(word)
	
	return SearchAndReturnID(listofterms)


def SearchAndReturnID(list_of_search_terms):
	yt_service = gdata.youtube.service.YouTubeService()
	query = gdata.youtube.service.YouTubeVideoQuery()
	query.orderby = 'relevance'
	query.text_query = ''
	tempquery =''
	for search_term in list_of_search_terms:
		new_term = search_term.lower()
		tempquery += '%s ' % search_term
	query.text_query = tempquery.encode('utf-8')
	#query.text_query = tempquery
	feed = yt_service.YouTubeQuery(query)
	return str(feed.entry[0].GetSwfUrl())
