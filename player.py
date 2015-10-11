import random

from card import Location, Unit, Supply, Order

# Deck
# @NOTE: Dealing with Duplicate Cards While Saving Decks; Use a Counter?
class Deck:

	'A stack of Cards for Play'

	def __init__(self, id_code, name, *cards):
		# Build Deck
		## Open Deck File
		## Construct Cards
		## Compile Deck
		#if not all(isinstance(card, Card) for card in cards):
		#	# Pass Exception
		# else:
		self.id_code = id_code
		self.name = name
		self.cards = cards # The stack of cards (as a List from top to bottom)

	# Load Deck from Disk
	def load(self):
		# @NOTE: Occurs at 'load' Player?
		pass

	# Save Deck to Disk
	def save(self):
		# @NOTE: Occurs at 'save' Player?
		pass

	# Shuffle
	def shuffle(self, t):
		[random.shuffle(self.cards) for _ in range(t)]

	# Draw
	def draw(self):
		return self.cards.pop(0)

	# Re-deck - Bottom
	def redeck_bottom(self, card):
		self.cards.append(card)

	# Re-deck - Top
	def redeck_top(self, card):
		self.cards.insert(0, card)

	# Reveal
	def reveal(self, i):
		return self.cards[i]

	# Select
	def select(self, i):
		return self.cards.pop(i)

	# Add Card
	# @NOTE: Use 'redeck_top'

	# Remove Card
	def remove(self, card):
		self.cards.remove(card)

# Player
class Player:

	'A player in the with decks of cards'

	def __init__(self, id_code, name, decks):
		id_code = ''
		name = ''
		decks = []

	# Load Deck from Disk
	def load(self):
		pass

	# Save Deck to Disk
	def save(self):
		pass

	# List Decks
	def list_deck_names(self):
		return [deck.name for deck in decks]