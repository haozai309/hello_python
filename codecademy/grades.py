grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# print all the grades
def print_grades(grades):
	for number in grades:
		print number

# sum of grades
def grades_sum(scores):
	total = 0
	for item in scores:
		total += item
	print total
	return total

# average grade
def grades_average(grades):
	return grades_sum(grades) / float(len(grades))

# variance
def grades_variance(scores):
	average = grades_average(scores)
	variance = 0
	for score in scores:
		variance += (average - score) ** 2
	variance /= len(scores)
	return variance

# standard deviation
def grades_std_deviation(variance):
	return variance ** 0.5

variance = grades_variance(grades)


print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)
