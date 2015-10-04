import random
from future import division

import Card

# Deck
class Deck:
	'A stack of Cards for Play'
	cards = []
	def __init__(*cards):
		# Build Deck
		## Open Deck File
		## Construct Cards
		## Compile Deck
		#if not all(isinstance(card, Card) for card in cards):
		#	# Pass Exception
		# else:
		self.cards = cards

	# Shuffle
	def shuffle(t):
		[random.shuffle(cards) for _ in range(t)]

	# Draw
	def draw():
		return cards.pop(0)

	# Re-deck - Bottom
	def redeck_bottom(card):
		cards.append(card)

	# Re-deck - Top
	def redeck_top(card):
		cards.insert(0, card)

	# Reveal
	def reveal(i):
		return cards[i]

	# Select
	def select(i):
		return cards.pop(i)

# Player
class Player:
	'A player in the game'
	id_code = ''
	name = ''
	decks = []
	stats = {
		'win':0,
		'loss':0,
		'draw':0,
		'resign':0
	}

	# Games Played
	def games_played():
		return sum(stats.intervalues())

	# Win Percentage
	def win_percent():
		return 0 if win == 0 else return float('{:1.3f}'.format(stat['win'] / games_played()))
