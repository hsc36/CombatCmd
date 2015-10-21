import json
import random
import jsonpickle as pickle

from card import *

# Deck
# @NOTE: Dealing with Duplicate Cards While Saving Decks; Use a Counter?
# Separate Deck and DeckList into seperate objects (one stores cards for game one stores card_ids for file saving)
class Deck:

	'A container of Cards for Play'

	def __init__(self, id_code=None, name=None, cards=None):
		# Build Deck
		## Open Deck File
		## Construct Cards
		## Compile Deck
		if not all(isinstance(card, Card) for card in cards):
			 raise ValueError('Deck can only contain Cards', [card for card in cards if not isinstance(card, Card)])
		# else:
		self.id_code = '' if id_code == None else id_code
		self.name = '' if name == None else name
		self.cards = [] if cards == None else cards # The stack of cards (as a List from top to bottom)

	# Load Deck from Disk
	def load(self, card_ids):
		if not isinstance(card_ids, list):
			card_ids = [card_ids]
		self.cards = [Card.load(card_id) for card_id in card_ids]

	# Save Deck to Disk
	# @NOTE: Instead, create a list of Card IDs and the number of duplicates
	def save(self):
		card_ids = [card.id_code for card in cards]
		self.cards = card_ids

	# Get Card List
	def list_card_ids(self):
		return [card.id_code for card in cards]

	# Shuffle
	def shuffle(self, t):
		[random.shuffle(self.cards) for _ in range(t)]

	# Draw
	def draw(self):
		return self.cards.pop(0)

	# Re-deck - Bottom
	def redeck_bottom(self, cards):
		if not isinstance(cards, list):
			card = [cards]
		[self.cards.append(card) for card in cards]

	# Re-deck - Top
	def redeck_top(self, cards):
		if not isinstance(cards, list):
			card = [cards]
		[self.cards.insert(0, card) for card in cards]

	# Reveal
	def reveal(self, card):
		return self.cards[card]

	# Select
	def select(self, card):
		return self.cards.pop(card)

	# Add Card
	# @NOTE: Use 'redeck_top'

	# Remove Card
	def remove(self, cards):
		if not isinstance(cards, list):
			card = [cards]
		[self.cards.remove(card) for card in cards]

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
			player = json.load(player_file)
			self.id_code = player['id_code']
			self.name = player['name']
			self.decks = [Deck.load(deck) for deck in player['decks']]

	# Save Deck to Disk
	def save(self):
		with open(__directory + '/' + id_code + '.' + __file_extension, 'w') as player_file:
			player = {}
			player['id_code'] = self.id_code
			player['name'] = self.name
			player['decks'] = Deck.save(decks)

	def new(self, name):
		self.id_code = generate_player_id(name) #@TODO: ID Generator
		self.name = name
		self.decks = []


	# List Decks
	def list_deck_names(self):
		return [deck.name for deck in decks]