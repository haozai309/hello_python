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


# remove the vowel characters in text
def anti_vowel(text):
	result = ""
	for char in text:
		if char.lower() not in ['a', 'e','i', 'o', 'u']:
			result += char
	print "anti_vowel of -%s- is -%s-" % (text, result)
	return result

anti_vowel("Hey You!")


# count the item occured in a list named sequence
def count(sequence, item):
	number = 0
	for element in sequence:
		if element == item:
			number += 1
	return number


# replace the word in text with same length of "*"
def censor(text, word):
	result = []
	for item in text.split():
		if item == word:
			item = "*" * len(item)
		result.append(item)
	return " ".join(result)

print censor("this hack is wack hack", "hack") 


# only keep then even number
def purify(numbers):
	result = []
	for num in numbers:
		if num > 1 and num % 2 == 0:
			result.append(num)
	return result







