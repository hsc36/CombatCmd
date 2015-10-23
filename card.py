from abc import ABCMeta, abstractmethod
import jsonpickle as pickle

# Card
class Card(object):

	'The abstract component of the game'

	__metaclass__ = ABCMeta

	def __init__(self, id_code, set_era, title, subtitle, type_name, effect):
		self.id_code = id_code	# Card Specific ID (based on Title/Subtitle/Set)
		self.set_era = set_era	# Card Set/Era
		self.title = title	# Card Title
		self.subtitle = subtitle	# Card Subtitle
		self.type_name = type_name	# Card Type
		self.effect = effect	# @NOTE: Need to extract line(s) of code from JSON database

	def __repr__(self):
		return '<' + str(type(self).__name__) + ': ' + ', '.join('%s=%s' % (k,v) for (k,v) in self.__dict__.iteritems()) + '>'

	def __str__(self):
		return type(self).__name__ + '(' + ', '.join('%s=%s' % (k,v) for (k,v) in self.__dict__.iteritems()) + ')'

	@abstractmethod
	def list_details(self):
		return [
			('Set', self.set_era),
			('Title', self.title),
			('Subtitle', self.subtitle),
			('Type', self.type_name),
			('Effect', self.effect)]

	# Load a Card, given its ID and the full dictionary of cards
	@abstractmethod
	def load(self, id_code, cards_dict):
		return pickle.decode(cards_dict[id_code])

	# Load a Card, given its particular sub-dictionary
	@abstractmethod
	def load(self, card_dict):
		return pickle.decode(card_dict)

	@abstractmethod
	def save(self):
		# JSONPickle the Card
		# Return the Card
		pass

## Location
class Location(Card):

	'Locations for staging Units and building up Supply'

	def __init__(self, id_code, set_era, title, subtitle, type_name, effect, storage, facility):
		Card.__init__(self, id_code, set_era, title, subtitle, type_name, effect)
		self.storage = storage	# Supply Storage Capacity
		self.facility = facility	# Unit Facility Size
	
	def list_details(self):
		return super(Location, self).list_details() + [
			('Storage', self.storage),
			('Facility', self.facility)]

## Unit
class Unit(Card):

	'Units for engaging in Combat'

	def __init__(self, id_code, set_era, title, subtitle, type_name, effect, size, supply_req, soft_attack, hard_attack, defense, is_hard_target):
		Card.__init__(self, id_code, set_era, title, subtitle, type_name, effect)
		self.size = size	# Uses Facilities
		self.supply_req = supply_req	# Uses Supplies
		self.soft_attack = soft_attack	# Soft Target Combat Damage Inflicted
		self.hard_attack = hard_attack	# Hard Target Combat Damage Inflicted
		self.defense = defense	# Combat Damage Required to Destroy this Unit
		self.is_hard_target = is_hard_target	# Attacker inflicts daage of a... False = Soft Target, True = Hard Target

	def list_details(self):
		return super(Unit, self).list_details() + [
			('Size', self.storage),
			('Supply Requirement', self.supply_req),
			('Soft Attack', self.soft_attack),
			('Hard Attack', self.hard_attack),
			('Defense', self.defense),
			('Hard Target', self.is_hard_target)]

## Supply
class Supply(Card):

	'Supplies for supporting Units'

	def __init__(self, id_code, set_era, title, subtitle, type_name, effect, size, supply):
		Card.__init__(self, id_code, set_era, title, subtitle, type_name, effect)
		self.size = size	# Uses Storage
		self.supply = supply	# Supplies for Units


	def list_details(self):
		return super(Supply, self).list_details() + [
			('Size', self.size),
			('Supply', self.supply)]

## Order
class Order(Card):
	
	'Adds bonuses and effects'
	
	def __init__(self, id_code, set_era, title, subtitle, type_name, effect, command):
		Card.__init__(self, id_code, set_era, title, subtitle, type_name, effect)
		self.command = command	# Cost of giving Orders

	def list_details(self):
		return super(Order, self).list_details() + [
			('Command', self.command)]

# Deck
# @NOTE_1: Dealing with Duplicate Cards While Saving Decks; Use Counter?
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

	###---Load/Save---###
	def sys(self):

		'System (Load/Save) Methods'

		# Make a Deck list from Cards in a Deck
		# @NOTE_1
		def list_card_ids(self):
			return [card.id_code for card in self.cards]

		# Make a list of Cards from Card IDs
		# @NOTE_1
		def from_list(self, card_ids):
			return [Card.load(card_id) for card_id in card_ids]

		# Make a list of Card IDs from a list of Cards
		# @NOTE_1
		def to_list(self):
			return [card.id_code for card in list_card_ids()]

		# Load a Deck
		def load(self, deck):
			self.id_code = deck.id_code
			self.name = deck.name
			self.cards = from_list(deck.cards)

		# Store a Deck (for saving)
		def store(self):
			deck = Deck()
			deck.id_code = self.id_code
			deck.name = self.name
			deck.cards = deck.to_list()
			return pickle.encode(deck)

	###---Deck Building---###
	def build(self):

		'Deck Construction'

		# Add Cards
		def add(*card_ids):
			if not isinstance(card_ids, list):
				card_ids = list(card_ids)
			self.cards.extend(card_ids)

		# Add 'x' amount of a Card for multiple Cards
		def robust_add(**card_ids_amounts):
			if not isinstance(card_ids_amounts, dict):
				card_ids_amounts = dict(card_ids_amounts)
			[add(card_id) for _ in xrange(amount) for card_id, amount in card_ids_amounts]

		# Remove Cards
		def remove(*card_ids):
			if not isinstance(card_ids, list):
				card_ids = list(card_ids)
			[self.cards.remove(card_id) for card_id in card_ids]

		# Remove 'x' amount of a Card for multiple Cards
		def robust_remove(**card_ids_amounts):
			if not isinstance(card_ids_amounts, dict):
				card_ids_amounts = dict(card_ids_amounts
			[remove(card_id) for _ in xrange(amount) for card_id, amount in card_ids_amounts]

	###---Gameplay---###
	def game(self):

		'Gameplay Methods'

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