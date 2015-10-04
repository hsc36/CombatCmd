# Card
class Card:
	'The basic component of the game'
	id_code = ''	# Card Specific ID (based on Title/Subtitle/Set)
	set_era = ''	# Card Set/Era
	title = ''	# Card Title
	subtitle = '' # Card Subtitle
	type_name = ''	# Card Type
	effect = '' # @NOTE: Need to extract line(s) of code from JSON database
	
	def __init__(self, id_code, set_era, title, subtitle, set_era):
		self.id_code = id_code
		self.set_era = set_era
		self.title = title
		self.subtitle = subtitle
		self.type_name = type_name
		self.effect = effect

## Location
class Location(Card):
	'Locations for staging Units and building up Supply'
	storage = 0	# Supply Storage Capacity
	facility = 0	# Unit Facility Size

	def __init__(storage, facility):
		Cards.__init__(self, id_code, set_era, title, subtitle, set_era):
		self.storage = storage
		self.facility = facility

## Unit
class Unit(Card):
	'Units for engaging in Combat'
	size = 0	# Uses Facilities
	supply_req = 0	# Uses Supplies
	attack = 0	# Combat Damage Inflicted
	defense = 0	# Combat Damage Required to Destroy this Unit

	def __init__(size, supply_req, attack, defense):
		Cards.__init__(self, id_code, set_era, title, subtitle, set_era):
		self.size = size
		self.supply_req = supply_req
		self.attack = attack
		self.defense = defense

## Supply
class Supply(Card):
	'Supplies for supporting Units'
	size = 0	# Uses Storage
	supply = 0	# Supplies for Units

	def __init__(size, supply):
		Cards.__init__(self, id_code, set_era, title, subtitle, set_era):
		self.size = size
		self.supply = supply

## Order
class Order(Card):
	'Adds bonuses and effects'
	command = 0	# Cost of giving Orders

	def __init__(command):
		Cards.__init__(self, id_code, set_era, title, subtitle, set_era):
		self.command = command