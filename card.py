# Card
class Card(object):

	'The basic component of the game'

	def __init__(self, id_code, set_era, title, subtitle, type_name, effect):
		self.id_code = id_code	# Card Specific ID (based on Title/Subtitle/Set)
		self.set_era = set_era	# Card Set/Era
		self.title = title	# Card Title
		self.subtitle = subtitle	# Card Subtitle
		self.type_name = type_name	# Card Type
		self.effect = effect	# @NOTE: Need to extract line(s) of code from JSON database

	def __repr__(self):
		return '{' + type(self).__name__ + ': ' + str(self.__dict__) + '}'

	def __str__(self):
		return type(self).__name__ + '(' + ', '.join('%s: %s' % (k,v) for (k,v) in self.__dict__.iteritems()) + ')'

	def list_details(self):
		return [
			('Set', self.set_era),
			('Title', self.title),
			('Subtitle', self.subtitle),
			('Type', self.type_name),
			('Effect', self.effect)]

## Location
class Location(Card):

	'Locations for staging Units and building up Supply'

	def __init__(self, id_code, set_era, title, subtitle, type_name, effect, storage, facility):
		Card.__init__(self, id_code, set_era, title, subtitle, type_name, effect)
		self.storage = storage	# Supply Storage Capacity
		self.facility = facility	# Unit Facility Size
	
	# @Override
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

	# @Override
	def list_details(self):
		return super(Location, self).list_details() + [
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

		# @Override
	def list_details(self):
		return super(Location, self).list_details() + [
			('Size', self.size),
			('Supply', self.supply)]

## Order
class Order(Card):
	
	'Adds bonuses and effects'
	
	def __init__(self, id_code, set_era, title, subtitle, type_name, effect, command):
		Card.__init__(self, id_code, set_era, title, subtitle, type_name, effect)
		self.command = command	# Cost of giving Orders

	# @Override
	def list_details(self):
		return super(Location, self).list_details() + [
			('Command', self.command)]