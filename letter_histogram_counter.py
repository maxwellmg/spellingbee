'''Program capable of taking a list of words, crossreferences letters of word with dict with empty values, and temporarily makes histogram of letters contained within that word. Used to determine exact number of unique letters per word and make a "panagram" list'''


def panagram_dictionary_creator():
    panagrams = []
    word_counter = 0
    with open('all_words_alpha.txt', 'r') as full_dictionary:
        for word in full_dictionary:
            word = word.strip('\n')
            letter_histogram = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
            unique_letter_counter = 0
            for letter in word:
                for key in letter_histogram:
                    if key == letter:
                        letter_histogram[key] = letter_histogram[key] + 1
                    else:
                        pass
                else:
                    pass
            for key in letter_histogram:
                if letter_histogram[key] == 0:
                    pass
                else:
                    unique_letter_counter +=1
            if unique_letter_counter == 7:
                word_counter +=1
                panagrams.append(word)
            else:
                pass
        #print(panagrams)
        print(word_counter)
        full_dictionary.close()

    f = open("panagram_dictionary2.txt", "a")
    for panagram in panagrams:
        f.write('"' + panagram + '", ')
    f.close()

panagram_dictionary_creator()
