from retrieveSimilar import *
from Artist import *
from retrieveSongs import *

class musicdiscclass:
	listofartists = []
	
	def searchArtistsandSongs(self,seed):
		getEchoNestArtists(seed, self.listofartists,'similar')
		
		getEchoNestSongs(self.listofartists)


