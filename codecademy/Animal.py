# Class definition
class Animal(object):
	"""Makes cute animals."""
	is_alive = True
	health = "good"
	# For initializing our instance objects
	def __init__(self, name, age, is_hungry):
		self.name = name
		self.age = age
		self.is_hungry = is_hungry

	def description(self):
		print self.name
		print self.age

# Note that self is only used in the __init__()
# fuction definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giaffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry, zebra.is_alive
print giaffe.name, giaffe.age, giaffe.is_hungry, giaffe.is_alive
print panda.name, panda.age, panda.is_hungry, panda.is_alive


tiger = Animal("Tiger", 5, False)
tiger.description()


hippo = Animal("Jake", 12, False)
sloth = Animal("sloth", 3, True)
ocelot = Animal("ocelot", 5, False)

print hippo.health

sloth.health = "bad"

print sloth.health
print ocelot.health








