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
		return pickled.decode(cards_dict[id_code])

	# Load a Card, given its particular sub-dictionary
	@abstractmethod
	def load(self, card_dict):
		return pickled.decode(card_dict)

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