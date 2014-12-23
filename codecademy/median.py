def median(numbers):
	numbers = sorted(numbers)
	length = len(numbers)
	if 	length % 2 == 0:
		return (numbers[length/2-1] + numbers[length/2])/2.0
	else:
		return numbers[(length-1)/2]

print median([1, 1, 2])
print median([4, 5, 5, 4])