import random

from Card import Location, Unit, Supply, Order

# Deck
# @NOTE: Dealing with Duplicate Cards While Saving Decks; Use a Counter?
class Deck:
	'A stack of Cards for Play'
	def __init__(self, *cards):
		# Build Deck
		## Open Deck File
		## Construct Cards
		## Compile Deck
		#if not all(isinstance(card, Card) for card in cards):
		#	# Pass Exception
		# else:
		self.cards = cards # The stack of cards (as a List from top to bottom)

	# Load Deck from Disk
	def load():

	# Save Deck to Disk
	def save():

	# Shuffle
	def shuffle(t):
		[random.shuffle(self.cards) for _ in range(t)]

	# Draw
	def draw():
		return self.cards.pop(0)

	# Re-deck - Bottom
	def redeck_bottom(card):
		self.cards.append(card)

	# Re-deck - Top
	def redeck_top(card):
		self.cards.insert(0, card)

	# Reveal
	def reveal(i):
		return self.cards[i]

	# Select
	def select(i):
		return self.cards.pop(i)

	# Add Card
	# @NOTE: Use 'redeck_top'

	# Remove Card
	def remove(card):
		self.cards.remove(card)

# Player
class Player:
	def __init__(self, id_code, name, decks):
		'A player in the game'
		id_code = ''
		name = ''
		decks = []

	# Load Deck from Disk
	def load():

	# Save Deck to Disk
	def save():