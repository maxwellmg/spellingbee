'''1. Create a list of eligible words
  a. Find a dictionary of just words
	To speed it up, find a list of 7 or more letter words
  b. Create a list where each letter is one item
  c. create a histogram program that counts the number of instances for each letter in each word. If a word hits >= 8 different items from the letter list, its ineligible.'''

#Program to narrow down dictionary

letter_list = ("abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi")


'''def seven_letter_words_program():
	seven_letter_words = []
	for word in letter_list:
		if len(word) < 7:
			pass
		else:
			print(word)
			seven_letter_words.append(word)
	print(seven_letter_words)

seven_letter_words_program()'''

def read_doc():
	seven_letter_word_dictionary = []
	word_counter = 0
	with open('all_words_alpha.txt', 'r') as rf:
		for word in rf:
			if len(word) < 1:
				pass
			else:
				word_counter +=1
				#new_word = word.strip('\n')
				#seven_letter_word_dictionary.append(new_word)
		print(word_counter)
		#print(seven_letter_word_dictionary)
		rf.close()

read_doc()

'''with open('seven_letter_words_txt', 'w') as wf:
	wf.write(seven_words)
	wf.close()'''
