grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
	for number in grades:
		print number

print_grades(grades)

def grades_sum(scores):
	total = 0
	for item in scores:
		total += item
	print total
	return total

print grades_sum(grades)


def grades_average(grades):
	return grades_sum(grades) / float(len(grades))

print grades_average(grades)

def grades_variance(scores):
	average = grades_average(scores)
	variance = 0
	for score in scores:
		variance += (average - score) ** 2
	variance /= len(scores)
	return variance

print grades_variance(grades)

