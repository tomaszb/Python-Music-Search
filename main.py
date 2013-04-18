import cgi, datetime, urllib, wsgiref.handlers, os

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext.webapp import template

import gdata.youtube
import gdata.youtube.service
import gdata.alt.appengine

from musicdisc import *

import logging
user = None

maxsong = 3

class MainPage(webapp.RequestHandler):
	def get(self):
		if users.get_current_user():
			user = users.get_current_user()
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			self.response.out.write("""
				<html>
					<body>
						<meta name="google-site-verification" content="QjEgVpXfGHD_PXskB7iaaf_nRCHbqt0cPIZiyq8wgiI" />
						<form action="/search" method="post">
						<div><input name="seed" type="text"></input></div>
						<div><input type="submit" value="Search for Artists"></div>
						</form>
					</body>
				</html>
				""")

		else:
			self.redirect(users.create_login_url(self.request.uri))

class Search(webapp.RequestHandler):
	def post(self):
		discInst.searchArtistsandSongs(cgi.escape(self.request.get('seed')))
		self.response.out.write('<html><body>Similar songs:<pre>')
		for artist in discInst.listofartists:
			for x in range(0, maxsong):
				self.response.out.write("%s - %s \n" % (artist.name, artist.songs[x]))
		#self.response.out.write("""
		#				<form action="/playlist" method="post">
		#				<div><input type="submit" value="Make Playlist!" </div> 
		#				</form>
		#				""")
		self.response.out.write('</pre></body></html>')

class Playlist(webapp.RequestHandler):
	def post(self):
		embedurl = searchandAdd(discInst.listofartists[0].name, discInst.listofartists[0].songs[0])
		
		#embedurl = "http://www.youtube.com/embed/%s?autoplay=1" % videoid

#		self.response.out.write("""
#				<html><body>
#				<iframe id="ytplayer" type="text/html" width="640" height="390"
#  src="%s"
#  frameborder="0"/></body></html>
#			""" % embedurl)
		self.response.out.write("""
				<html><body>
				<div id="player"></div>

			    <script src="http://www.youtube.com/player_api"></script>

			    <script>

			        // create youtube player
			        var player;
			        function onYouTubePlayerAPIReady() {
			            player = new YT.Player('player', {
			              height: '390',
			              width: '640',
			              videoId: '0Bmhjf0rKe8',
			              events: {
			                'onReady': onPlayerReady,
			                'onStateChange': onPlayerStateChange
			              }
			            });
			        }

			        // autoplay video
			        function onPlayerReady(event) {
			            event.target.playVideo();
			        }

			        // when video ends
			        function onPlayerStateChange(event) {        
			            if(event.data === 0) {          
			                alert('done');
			            }
			        }

			    </script>
				</html></body>
			""")

def main():
	logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
	app = webapp.WSGIApplication([('/', MainPage),
								('/search', Search),
								('/playlist', Playlist)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)


if __name__ == "__main__":
    main()
