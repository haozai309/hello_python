
my_dict = {
	"name" : "Leo",
	"hobby": "Yoga",
	"wish" : "retirement"
}

print my_dict.items()

for key in my_dict:
	print key, my_dict[key]


evens_to_50 = [i for i in range(51) if i % 2 == 0]

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1, 12) if x % 2 == 0]
print even_squares

cubes_by_four = [x**3 for x in range(1, 11) if (x**3) % 4 == 0]
print cubes_by_four

# list[start:end:stride]
#   default:
#       0 len()-1   1
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]


# test the strides
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens


to_21 = range(1, 22)
#odds = [i for item in to_21 if item % 2 == 1]
odds = to_21[::2]
middle_third = to_21[7:14]

