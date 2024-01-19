#wrong_word_eliminator
#words cannot be less than 4 letters, and they cannot have more than 7 unique letters. This program will pare down the dictionary before we make it do all the heavy lifting of finding all elligible words for each panagram

def wrong_word_eliminator():
    viable_words = []
    word_counter = 0
    with open('all_words_alpha.txt', 'r') as full_dictionary:
        for word in full_dictionary:
            word = word.strip('\n')
            letter_histogram = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
            unique_letter_counter = 0
            if len(word) < 4:
                print(word + " is less than 4 characters")
                pass
            else:
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
                if unique_letter_counter > 7:
                    print(word + " has too many unique characters")
                    pass
                else:
                    word_counter +=1
                    viable_words.append(word)
        print(word_counter)
        full_dictionary.close()

    f = open("all_words_beta_list.txt", "a")
    for word in viable_words:
        f.write('"' + word + '", ')
    f.close()

wrong_word_eliminator()

#took full word list down from 370,103 words to 188,586 words