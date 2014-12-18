def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False


def is_int(x):
	if x < 0:
		x *= -1
	if x % 1 > 0:
		return False
	else:
		return True

def digit_sum(n):
	total = 0
	while True:
		total += n % 10
		if n / 10 > 0:
			n = n / 10
		else:
			return total

def factorial(x):
	if x == 1:
		return x
	else:
		return x * factorial(x-1)

def is_prime(x):
	if x < 2:
		return False
	else:
		for num in range(2, x):
			if x % num == 0:
				return False
		return True

# text[::-1] is also OK
def reverse(text):
	result = ""
	for i in range(len(text)-1, -1, -1):
		result += text[i]
	return result


def anti_vowel(text):
	result = ""
	for char in text:
		if char.lower() not in ['a', 'e','i', 'o', 'u']:
			result += char
	print "anti_vowel of -%s- is -%s-" % (text, result)
	return result

anti_vowel("Hey You!")









