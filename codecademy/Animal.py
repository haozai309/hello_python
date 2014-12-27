# Class definition
class Animal(object):
	"""Makes cute animals."""
	# For initializing our instance objects
	def __init__(self, name, age, is_hungry):
		self.name = name
		self.age = age
		self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# fuction definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giaffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giaffe.name, giaffe.age, giaffe.is_hungry
print panda.name, panda.age, panda.is_hungry
