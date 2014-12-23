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

grades_sum(grades)
