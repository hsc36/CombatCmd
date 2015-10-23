import json
import random
import jsonpickle as pickle

from card import Deck

# Player
class Player:

	'A player with decks of cards'

	__directory = '/players'
	__file_extension = 'json'	# File extension for Player files

	def __init__(self, id_code=None, name=None, decks=None):
		self.id_code = '' if id_code == None else id_code
		self.name = '' if name == None else name
		self.decks = [] if decks == None decks

	# Load Deck from Disk
	def load(self, id_code):
		with open(__directory + '/' + id_code + '.' + __file_extension) as player_file:
			player = pickle.decode(player_file)
			self.id_code = player.id_code
			self.name = player.name
			self.decks = [Deck.from_list(deck) for deck in player.decks]

	# Save Deck to Disk
	def save(self):
		with open(__directory + '/' + id_code + '.' + __file_extension, 'w') as player_file:
			pickle.encode(self)

	# Create a new Player
	def new(self, name):
		self.id_code = generate_player_id(name) #@TODO: ID Generator, based on type()
		self.name = name
		self.decks = []

	# List Deck Names
	def list_deck_names(self):
		return [deck.name for deck in self.decks]

	# List Deck IDs
	def list_deck_ids(self):
		return [deck.id_code for deck in self.decks]

	# Add a Deck

	# Remove a Deck