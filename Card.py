# Card
class Card:
	'The basic component of the game'
	id_code = ''	# Card Specific ID (based on Title/Subtitle/Set)
	set_era = ''	# Card Set/Era
	title = ''	# Card Title
	subtitle = '' # Card Subtitle
	type_name = ''	# Card Type
	
	def __init__(self, id_code, set_era, title, subtitle, set_era):
		self.id_code = id_code
		self.set_era = set_era
		self.title = title
		self.subtitle = subtitle
		self.type_name = type_name

## Location
class Location:
	'Locations for staging Units and building up Supply'
	storage = 0	# Supply Storage Capacity
	facilities = 0	# Unit Facility Capacity
	effect = '' # @NOTE: Need to extract line(s) of code from JSON database

## Unit


## Supply


## Command