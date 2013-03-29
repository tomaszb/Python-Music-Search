import cgi, datetime, urllib, wsgiref.handlers, os

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext.webapp import template

from musicdisc import *

import logging

class MainPage(webapp.RequestHandler):
	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			self.response.out.write("""
				<html>
					<body>
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
		disc = musicdiscclass()
		disc.searchArtistsandSongs(cgi.escape(self.request.get('seed')))
		self.response.out.write('<html><body>Similar artists:<pre>')
		for artist in disc.listofartists:
			self.response.out.write(artist.name + "\n")
		self.response.out.write("""
						<form action="/playlist" method="post">
						<div><input type="submit" value="Make Playlist!" </div> 
						</form>
						""")
		self.response.out.write('</pre></body></html')

class Playlist(webapp.RequestHandler):
	def post(self):
		self.response.out.write("""
				<html><body>Made playlist!</body></html>
			""")


def main():
	app = webapp.WSGIApplication([('/', MainPage),
								('/search', Search),
								('/playlist', Playlist)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)


if __name__ == "__main__":
    main()
