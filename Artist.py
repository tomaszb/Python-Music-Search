import json, pprint

class Artist:
	def __init__(self, _name, _id):
		self.name = _name
		self.id = _id
		self.songs = []

	def addSongs(self,_songs):
		for s in _songs:
			if (not(s in self.songs)):
				self.songs.append(s)

	def count():
		return len(self.songs)