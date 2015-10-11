from player import Deck, Player
from datetime import datetime as dt

class Session(object):

	'A Game Session for creating a player, building/modifying a deck, or playing a game'

	def __init__(self):
		self.__start_time = dt.utcnow()


	# Universal diplay function, for all STDOUT
	def display(*args):
		for i, x in enumerate(args):
			print str(i) + '. ' + x

	def get_player():
		# Create or Load
		# Get Player Name
		# Get a Deck
		# Save Player and Deck(s)

	def get_deck(player):
		# Load Player
		# Load or Create Deck
		# - Modify a Saved Deck > Load the Deck
		# - Create a New Deck
		# Save the Deck
		# Save the Player

	def play_game(*player):
		# Each Player Chooses a Deck
		# Determine Turn Order
		# Game Setup Steps
		# Gameplay
		# Game Result