class NWStates:
	'Base class for all states'
	statecount = 0
	citycount = 0
	
	def __init__(self, name, population, area, location):
		self.name = name
		self.population = population
		self.area = area
		self.location = location
		NWStates.statecount += 1
		
	def displayStateCount(self):
		print("Total number of states included: {}".format(NWStates.statecount))

#	def founding(self):
#		return "{} was founded in 1889".format(Washington.name)
#		return "{} was founded in 1859".format(Oregon.name)

Washington = NWStates("Washington", 7405743, 71362, "NW")
Oregon = NWStates("Oregon", 4142776, 98381, "NW")

if Washington.location == "NW":
	print("{} is a state in the NW".format(Washington.name))
if Oregon.location == "NW":
	print("{} is a state in the NW".format(Oregon.name))

def biggest_pop(*args):
	return max(args)

print("Total number of states included: {}".format(NWStates.statecount))

print("The most populated state has {} people.".format(biggest_pop(Washington.population, 
Oregon.population)))


class NWCities(NWStates):
	'Subclass for all cities'

	def displayCityCount(self):
		print("Total number of cities included: {}".format(NWCities.citycount))
	
	def rainfall(self, inches):
		self.inches = inches


Seattle = NWCities("Seattle", 713700, 142.5, "Washington")
Portland = NWCities("Portland", 647805, 145, "Oregon")
Spokane = NWCities("Spokane", 217300, 60.02, "Washington")

setattr(Seattle, 'rainfall', 37.5)
setattr(Portland, 'rainfall', 36.69)
setattr(Spokane, 'rainfall', 16.5)

if Seattle.location == "Washington":
	NWCities.citycount += 1
	print("{} is a city in the NW".format(Seattle.name))
if Portland.location == "Oregon":
	NWCities.citycount += 1
	print("{} is a city in the NW".format(Portland.name))
if Spokane.location == "Washington":
	NWCities.citycount += 1
	print("{} is a city in the NW".format(Spokane.name))

print("Total number of cities included: {}".format(NWCities.citycount))

def most_rain(*inches):
	return max(inches)

print("The wettest city has {} in of rain yearly.".format(most_rain(Seattle.rainfall,
Portland.rainfall)))

def biggest_city(*area):
	return max(area)

print("The largest city is {} sq mi.".format(biggest_city(Seattle.area,
Portland.area)))

