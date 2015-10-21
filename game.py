from player import Deck, Player
from datetime import datetime as dt

class Session(object):

	'A Game Session for creating a player, building/modifying a deck, or playing a game'

	def __init__(self):
		self.__start_time = dt.utcnow()


	def display_numbered_list(self, l):
		for i, x in enumerate(l):
			print str(i) + '. ' + x

	def display_card_details(self, details):
		for detail in details:
			print str(detail[0]) + ': ' + str(detail[1])

	def get_player(self):
		pass
		# Create or Load
		# Get Player Name
		# Get a Deck
		# Save Player and Deck(s)

	def get_deck(self, player):
		pass
		# Load Player
		# Load or Create Deck
		# - Modify a Saved Deck > Load the Deck
		# - Create a New Deck
		# Save the Deck
		# Save the Player

	def play_game(self, *player):
		pass
		# Each Player Chooses a Deck
		# Determine Turn Order
		# Game Setup Steps
		# Gameplay
		# Game Result