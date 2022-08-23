# Function to reverse words of string
import re
def rev_sentence(sentence):

	# find all the words in sentence
	words = re.findall('\w+', sentence)

	# Backward iterate over list of words and join using space
	reverse_sentence = ' '.join(words[i] for i in range(len(words)-1, -1, -1))

	# finally return the joined string
	return reverse_sentence

if __name__ == "__main__":
	input = 'geeks quiz practice code'
	print (rev_sentence(input))

