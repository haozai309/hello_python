# Pig Latin is a language game, where you move the first  letter of the word to the end and add "ay." So "Python" becomes "ythonpay."

def converter(input):
    if len(input) > 1:
        print input[1:] + input[0] + "ay"

print "Welcome to the Pig Latin Translator!"
print "Let's play a game named 'Pig Latin'"
answer = raw_input("Please input a word you like: ")
converter(answer)
